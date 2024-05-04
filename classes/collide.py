from player import Player

class QuadTree:

    def __init__(self, items : list, base_nr : int, x: int, y: int, 
                       width: int, height: int) -> None:
        """ This class expects an list of items which all have a 
            .pos = np.array([x : int, y : int]).
        """

        # Create two list of the items, ordered in x, y respectively.
        items_x = sorted(items, key=lambda e: e.pos[0])
        items_y = sorted(items, key=lambda e: e.pos[1])

        # Calculate split points.
        split_point_x = x + width / 2
        split_point_y = y + height / 2

        # Split the two sorted list.
        items_x_splits, items_y_splits = [], []
        for i, lis in enumerate([items_x, items_y]):
            print("i=",i)
            half_index = int(len(lis) / 2)
            el = lis[half_index]
            print(el.pos[i])
            split_point = [split_point_x, split_point_y][i]
            direction = int((-1)**(int(el.pos[i] > split_point)))


            print([it.pos[i] for it in lis[int((1+direction)/2*half_index) : int(len(lis) - (1-direction)/2*half_index)][::direction]])
            for item in lis[int((1+direction)/2*half_index) : 
                            int(len(lis) - (1-direction)/2*half_index)][::direction]:
                print(item.pos[i])

                if direction*item.pos[i] > direction*split_point:
                    low = lis[:lis.index(item)]
                    high = lis[lis.index(item):]
                    [items_x_splits, items_y_splits][i] = [low, high]
                    break

        # Create four quartiles.
        print(items_x_splits)
        print(items_y_splits)
        nw = list(set(items_x_splits[0]).intersection(items_y_splits[0]))
        ne = list(set(items_x_splits[1]).intersection(items_y_splits[0]))
        sw = list(set(items_x_splits[0]).intersection(items_y_splits[1]))
        se = list(set(items_x_splits[1]).intersection(items_y_splits[1]))

        print(nw)
        print(ne)
        print(sw)
        print(se)





if __name__ == '__main__':
    q = QuadTree([Player(0,0), Player(0,10), Player(10,10),  Player(10,0)], 1, 0, 0, 10, 10)
