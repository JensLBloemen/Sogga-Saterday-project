import numpy as np


class Arrow:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.pos = np.array([x, y])
        self.direction = np.array(direction)
        self.speed = 10