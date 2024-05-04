

class Sogga:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.velocity = [1, 1]

    def zabloing(self):
        print(f"{self.name} zabloing!")
