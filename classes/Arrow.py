import numpy as np


class Arrow:
    def __init__(self, x, y, direction):
        self.length = 100
        self.pos = np.array([x, y])
        self.original_pos = self.pos.copy()
        self.direction = np.array(direction)
        self.speed = 10

        self.update_counter = 0

    def update(self):
        self.update_counter += 1
        self.pos = self.original_pos + np.array([int(i * self.update_counter) for i in self.direction * self.speed])
        if self.update_counter > 100:
            return False
        return True 
