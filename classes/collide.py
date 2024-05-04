from player import Player

class QuadTree:

    def __init__(self, items : list, base_nr : int, x: int, y: int, 
                       width: int, length: int) -> None:
        """ This class expects an list of items which all have a 
            .pos = np.array([x : int, y : int]).
        """

        # Create two list of the items, ordered in x, y respectively.
        items_x = sorted(items, key=lambda e: e.pos[0])
        items_y = sorted(items, key=lambda e: e.pos[1])

        # Calculate split points.
        split_x = x + width / 2
        split_y = y + width / 2

        # Split the two sorted list.
        for i, lis in enumerate([items_x, items_y]):
            el = lis[int(len(lis) / 2)]
            split = [split_x, split_y][i]
            direction = (-1)**(int(el.pos[i] > split))
            for item in lis[1-direction :  : direction]
            
                



if __name__ == '__main__':
    q = QuadTree([Player(0,0), Player(0,1), Player(1,1),  Player(1,0)], 1, 0, 0, 1, 1)
