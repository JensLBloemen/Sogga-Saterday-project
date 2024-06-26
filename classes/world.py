from classes.player import Player
from classes.fixture import Fixture
from classes.Arrow import Arrow

from data.animation_list import animation_list

import socket
import threading
import numpy as np

from player_pb2 import Player as pb_Player  # Import your generated protobuf classes
from player_pb2 import Arrow as pb_Arrow    # Import your generated protobuf classes
from player_pb2 import Arrows as pb_Arrows  # Import your generated protobuf classes

# Wereld gaat conact hebben met server. Stuurt player info en krijgt other player info

class World:

    def __init__(self) -> None:

        self.can_reach_server = True

        self.server_address = ("192.168.178.36", 5555)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        receiver_thread = threading.Thread(target=self.listen_for_messages, args=(self.sock,))
        receiver_thread.start()

            # send_messages(sock, server_address)   

        self.width = 2048
        self.height = 2048
        self.player = None
        self.other_players = {}
        self.fixtures = [] # this stays 1 list with diff types of fixtures.

        self.arrows = []

        # Add fixtures.
        self.add_fixture(0, 0, 50, 500)
        self.add_fixture(1000, 0, 50, 500)


    def listen_for_messages(self, sock):
        while True:
            data, _ = sock.recvfrom(4096)
            player = pb_Player()
            player.ParseFromString(data)
            if player.id not in self.other_players:
                print(f"New player added!:{player.name} id:{player.id}")
                
            other_player = Player(player.position.x, player.position.y, player.name)
            other_player.anim_id = player.anim_id
            other_player.rotation = player.rotation
            
            other_player.arrows = [Arrow(arr.position.x, arr.position.y, (arr.direction.x, arr.direction.y), arr.speed) for arr in player.arrows.arrows]
            self.other_players[player.id] = other_player


    def add_player(self, x : int, y : int, name : str) -> Player:
        """ Add a player to the game and return the player to creator. """
        new_player = Player(x, y, name)
        self.player = new_player
        return self.player

    # Replace later for different specific types of fixtures
    def add_fixture(self, x : int, y : int, width : int, height : int) -> None:
        self.fixtures.append(Fixture(x, y, width, height))

    def add_arrow(self, x, y, direction, speed):
        x += direction[0] * Arrow.length
        y += direction[1] * Arrow.length
        self.arrows.append(Arrow(x, y, direction, speed))

    def move_player(self, vel):
        self.player.move(vel)

        # Correct out of world. Could be deleted if world is surounded by fixtures.
        if self.player.pos[0] < 0: self.player.pos[0] = 0
        if self.player.pos[1] < 0: self.player.pos[1] = 0
        if self.player.pos[0] > self.width: self.player.pos[0] = self.width
        if self.player.pos[1] > self.height: self.player.pos[1] = self.height

        # Check of collision with fixtures.
        player_lowx = self.player.pos[0] - self.player.radius
        player_lowy = self.player.pos[1] - self.player.radius
        player_highx = self.player.pos[0] + self.player.radius
        player_highy = self.player.pos[1] + self.player.radius
        for fixture in self.fixtures:
            fix_lowx = fixture.pos[0]
            fix_lowy = fixture.pos[1]
            fix_highx = fixture.pos[0] + fixture.width
            fix_highy = fixture.pos[1] + fixture.height

            left_col = player_lowx < fix_lowx and fix_lowx < player_highx
            right_col = fix_lowx < player_lowx and player_lowx < fix_highx
            up_col = player_lowy < fix_lowy and fix_lowy < player_highy
            down_col = fix_lowy < player_lowy and player_lowy < fix_highy

            if (left_col or right_col) and (up_col or down_col):
                self.player.undo_movement()
        
        for player in self.other_players.values():
            # Check for collision with players.
            if np.linalg.norm(self.player.pos - player.pos) < self.player.radius + player.radius:
                self.player.undo_movement()

            # Check for collision with arrows.
            for arrow in player.arrows:
                if np.linalg.norm(self.player.pos - arrow.pos) < self.player.radius:
                    self.player.hurt(arrow)
                    print("Arrow hit!")


    def update(self) -> None:
        """ Update world. """

        player = pb_Player()

        to_kill = []
        for arrow in self.arrows:
            if not arrow.update():
                to_kill.append(arrow)
        
        for arrow in to_kill:
            self.arrows.remove(arrow)

        player.id = self.player.id
        player.name = self.player.name
        player.position.x = self.player.pos[0]
        player.position.y = self.player.pos[1]
        player.rotation = self.player.rotation
        player.anim_id = self.player.anim_id


        arrows = pb_Arrows()
        for selfarrow in self.arrows:
            arrow = pb_Arrow()
            arrow.speed = int(selfarrow.speed)
            arrow.position.x = int(selfarrow.pos[0])
            arrow.position.y = int(selfarrow.pos[1])
            arrow.direction.x = selfarrow.direction[0]
            arrow.direction.y = selfarrow.direction[1]
            arrows.arrows.append(arrow)

        player.arrows.CopyFrom(arrows)



        data = player.SerializeToString()
        if self.can_reach_server:
            try:
                self.sock.sendto(data, self.server_address)
            except OSError:
                print("Can't reach server bozo!\nTurn on your wifi")
                self.can_reach_server = False

