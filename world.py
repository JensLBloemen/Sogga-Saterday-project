from player import Player
from fixture import *

# Wereld gaat conact hebben met server. Stuurt player info en krijgt other player info

class World:

    def __init__(self) -> None:
        self.player = None
        self.other_players = []
        self.fixtures = [] # this stays 1 list with diff types of fixtures.

        # Add fixtures.
        self.add_fixture(300, 0, 50, 50)
        self.add_fixture(-300, 0, 50, 50)
        self.add_fixture(0, 300, 50, 50)
        self.add_fixture(0, -300, 50, 50)

        
    def add_player(self, x, y) -> Player:
        """ Add a player to the game and return the player to creator. """
        new_player = Player(x, y)
        self.players = new_player
        return new_player

    # Replace later for different specific types of fixtures
    def add_fixture(self, x, y, width, height) -> None:
        self.fixtures.append(Fixture(x, y, width, height))