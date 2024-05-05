import numpy as np


class Arrow:
    length = 100
    def __init__(self, x, y, direction, speed):
        self.pos = np.array([x, y])
        self.original_pos = self.pos.copy()
        self.direction = np.array(direction)
        self.speed = speed
        self.range = 400

        self.update_counter = 0
        self.life = 80

    def update(self):
        self.update_counter += 1
        self.pos = self.original_pos + np.array([int(i * min(self.update_counter, self.life)) for i in self.direction * self.speed])
        if self.update_counter > self.range:
            return False
        return True 
