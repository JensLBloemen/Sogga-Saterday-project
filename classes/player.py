import numpy as np

class Player:

    def _init_(self, x, y) -> None:
        self.pos = np.array([x, y])
        self.speed = 5
        self.radius = 30
        self.last_pos = np.array([x, y])

    def move(self, direction : np.array) -> None:
        self.last_pos = self.pos.copy()
        self.pos += direction * self.speed

    def undo_movement(self):
        self.pos = self.last_pos
