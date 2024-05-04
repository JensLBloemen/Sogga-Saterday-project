from classes.player import Player
from classes.fixture import Fixture

# Wereld gaat conact hebben met server. Stuurt player info en krijgt other player info

class World:

    def __init__(self) -> None:
        self.width = 2000
        self.height = 2000
        self.player = None
        self.other_players = []
        self.fixtures = [] # this stays 1 list with diff types of fixtures.

        # Add fixtures.
        self.add_fixture(300, 0, 50, 50)
        self.add_fixture(-300, 0, 50, 50)
        self.add_fixture(0, 300, 50, 50)
        self.add_fixture(0, -300, 50, 50)


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
