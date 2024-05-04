import numpy as np

class Player:

    def __init__(self, x, y) -> None:
        self.pos = np.array([x, y])
        self.speed = 5
        self.radius = 30

    def move(self, direction : np.array) -> None:
        self.pos += direction * self.speed

