import numpy as np

class Player:
    radius = 45
    def __init__(self, x, y, name) -> None:
        self.name = name
        self.id = string_to_int(name)
        self.pos = np.array([x, y])
        self.speed = 5
        
        self.last_pos = np.array([x, y])
        self.hp = 100
        self.rotation = 0
        self.curr_animation = None
        self.anim_id = 0
        self.arrows_hit = set()

    def move(self, direction : np.array) -> None:
        self.last_pos = self.pos.copy()
        self.pos += direction * self.speed

    def undo_movement(self):
        self.pos = self.last_pos

    def hurt(self, arrow):
        if arrow not in self.arrows_hit:
            self.arrows_hit.add(arrow)
            self.hp -= arrow.speed // 2



def string_to_int(input_string):
    
    result = 0
    for char in input_string:
        result = result * 256 + ord(char)

    return result % 2 ** 31

