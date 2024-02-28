import random

from board import Board


class Game:

    def __init__(self, num_starting_tiles=2, spawn_values=(2, 4), spawn_probs=(0.9, 0.1)):
        self.board = Board()
        values = random.choices(spawn_values, weights=spawn_probs, k=num_starting_tiles)
        for value in values:
            self.board.add_tile(value)

        print(self.board.tiles)


if __name__ == '__main__':
    game = Game()