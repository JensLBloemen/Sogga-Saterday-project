import numpy as np

class Player:

    def __init__(self, x, y, name) -> None:
        self.name = name
        self.id = string_to_int(name)
        self.pos = np.array([x, y])
        self.speed = 5
        self.radius = 45
        self.last_pos = np.array([x, y])
        self.hp = 100

    def move(self, direction : np.array) -> None:
        self.last_pos = self.pos.copy()
        self.pos += direction * self.speed

    def undo_movement(self):
        self.pos = self.last_pos


def string_to_int(input_string):
    
    result = 0
    for char in input_string:
        result = result * 256 + ord(char)

    return result % 2 ** 31

