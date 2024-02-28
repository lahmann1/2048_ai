import numpy as np


class Board:

    def __init__(self, num_y=4, num_x=4):
        self.tiles = np.zeros((num_y, num_x), dtype=int)

    def add_tile(self, value):
        y_indexes, x_indexes = np.where(self.tiles == 0)
        n = np.random.randint(0, len(y_indexes), size=1)
        self.tiles[y_indexes[n], x_indexes[n]] = value

    def shift_up(self):
        # Get nonzero indexes
        y_indexes, x_indexes = self.tiles.nonzero()

        # Sort so that we go from top to bottom
        i = y_indexes.argsort()
        y_indexes = y_indexes[i]
        x_indexes = x_indexes[i]

        # Loop through all the tiles
        for y, x in zip(y_indexes, x_indexes):
            collision = False       # Only one collision per tile
            while True:
                if y == 0:
                    break
                if self.tiles[y-1][x] == 0:
                    self.tiles[y-1][x] = self.tiles[y][x]
                    self.tiles[y][x] = 0
                elif self.tiles[y-1][x] == self.tiles[y][x] and not collision:
                    self.tiles[y-1][x] *= 2
                    self.tiles[y][x] = 0
                    collision = True
                else:
                    break
                y -= 1

    def shift_down(self):
        # Get nonzero indexes
        y_indexes, x_indexes = self.tiles.nonzero()

        # Sort so that we go from bottom to top
        i = y_indexes.argsort()[::-1]
        y_indexes = y_indexes[i]
        x_indexes = x_indexes[i]

        # Loop through all the tiles
        for y, x in zip(y_indexes, x_indexes):
            collision = False       # Only one collision per tile
            while True:
                if y == self.tiles.shape[0] - 1:
                    break
                if self.tiles[y+1][x] == 0:
                    self.tiles[y+1][x] = self.tiles[y][x]
                    self.tiles[y][x] = 0
                elif self.tiles[y+1][x] == self.tiles[y][x] and not collision:
                    self.tiles[y+1][x] *= 2
                    self.tiles[y][x] = 0
                    collision = True
                else:
                    break
                y += 1

    def shift_left(self):
        # Get nonzero indexes
        y_indexes, x_indexes = self.tiles.nonzero()

        # Sort so that we go from left to right
        i = x_indexes.argsort()
        y_indexes = y_indexes[i]
        x_indexes = x_indexes[i]

        # Loop through all the tiles
        for y, x in zip(y_indexes, x_indexes):
            collision = False       # Only one collision per tile
            while True:
                if x == 0:
                    break
                if self.tiles[y][x-1] == 0:
                    self.tiles[y][x-1] = self.tiles[y][x]
                    self.tiles[y][x] = 0
                elif self.tiles[y][x-1] == self.tiles[y][x] and not collision:
                    self.tiles[y][x-1] *= 2
                    self.tiles[y][x] = 0
                    collision = True
                else:
                    break
                x -= 1

    def shift_right(self):
        # Get nonzero indexes
        y_indexes, x_indexes = self.tiles.nonzero()

        # Sort so that we go from right to left
        i = x_indexes.argsort()[::-1]
        y_indexes = y_indexes[i]
        x_indexes = x_indexes[i]

        # Loop through all the tiles
        for y, x in zip(y_indexes, x_indexes):
            collision = False       # Only one collision per tile
            while True:
                if x == self.tiles.shape[1] - 1:
                    break
                if self.tiles[y][x+1] == 0:
                    self.tiles[y][x+1] = self.tiles[y][x]
                    self.tiles[y][x] = 0
                elif self.tiles[y][x+1] == self.tiles[y][x] and not collision:
                    self.tiles[y][x+1] *= 2
                    self.tiles[y][x] = 0
                    collision = True
                else:
                    break
                x += 1


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
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    board.add_tile(2)
    print(board.tiles)
    board.shift_right()
    print(board.tiles)
