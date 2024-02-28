import numpy as np


class Board:

    def __init__(self, num_y=4, num_x=4):
        self.tiles = np.zeros((num_y, num_x), dtype=int)

    def add_tile(self, value):
        y_indexes, x_indexes = np.where(self.tiles == 0)
        n = np.random.randint(0, len(y_indexes), size=1)
        self.tiles[y_indexes[n], x_indexes[n]] = value

    def shift_up(self):
        y_indexes, x_indexes = np.where(self.tiles != 0)
        for y, x in zip(y_indexes, x_indexes):
            done = False
            while not done:
                if y == 0:
                    break
                if self.tiles[y-1][x] == 0:
                    self.tiles[y-1][x] = self.tiles[y][x]
                    self.tiles[y][x] = 0
                elif self.tiles[y-1][x] == self.tiles[y][x]:
                    self.tiles[y-1][x] *= 2
                    self.tiles[y][x] = 0
                else:
                    break
                y -= 1



if __name__ == '__main__':
    board = Board()
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    print(board.tiles)
    board.shift_up()
    print(board.tiles)
