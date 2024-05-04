from classes.player import Player
from classes.fixture import Fixture


import socket
import threading
import random
from player_pb2 import Player as pb_Player  # Import your generated protobuf classes

# Wereld gaat conact hebben met server. Stuurt player info en krijgt other player info

class World:

    def __init__(self) -> None:
        self.player_id = random.randint(1, 50)
        self.server_address = ("192.168.8.115", 5555)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        receiver_thread = threading.Thread(target=self.listen_for_messages, args=(self.sock,))
        receiver_thread.start()

            # send_messages(sock, server_address)   

        self.width = 2000
        self.height = 2000
        self.player = None
        self.other_players = {}
        self.fixtures = [] # this stays 1 list with diff types of fixtures.

        # Add fixtures.
        self.add_fixture(300, 0, 50, 50)
        self.add_fixture(-300, 0, 50, 50)
        self.add_fixture(0, 300, 50, 50)
        self.add_fixture(0, -300, 50, 50)


    def listen_for_messages(self, sock):
        while True:
            data, _ = sock.recvfrom(4096)
            player = pb_Player()
            player.ParseFromString(data)
            if player.id not in self.other_players:
                print(f"New player added!: {player.id}")
                
            self.other_players[player.id] = Player(player.position.x, player.position.y)
            print(f"Received message: ID={player.id}, Name={player.name}, Position=({player.position.x}, {player.position.y})")


    def add_player(self, x : int, y : int) -> Player:
        """ Add a player to the game and return the player to creator. """
        new_player = Player(x, y)
        self.player = new_player
        return self.player

    # Replace later for different specific types of fixtures
    def add_fixture(self, x : int, y : int, width : int, height : int) -> None:
        self.fixtures.append(Fixture(x, y, width, height))

    def move_player(self, vel):
        self.player.move(vel)
        # Check you out of world
        # Check of collision with fixture
        # Check for collision 
    

    def update(self) -> None:
        """ Update world. """

        print("Updating world...")
        player = pb_Player()
        player.id = self.player_id
        player.name = f"Player {self.player_id}"
        player.position.x = self.player.pos[0]
        player.position.y = self.player.pos[1]

        data = player.SerializeToString()
        self.sock.sendto(data, self.server_address)


    def kill(self):
        """ Kill the world. """
        self.sock.close()
        quit()

