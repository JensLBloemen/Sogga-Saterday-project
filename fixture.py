import numpy as np

# Replace later for different specific types of fixtures
class Fixture:

    def __init__(self, x, y, width, height) -> None:
        self.pos = np.array([x,y])
        self.width = width
        self.height = height
