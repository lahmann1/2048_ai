import random

from board import Board


class Game:

    def __init__(self, num_starting_tiles=2, spawn_values=(2, 4), spawn_probs=(0.9, 0.1)):
        self.board = Board()
        self.spawn_values = spawn_values
        self.spawn_probs = spawn_probs
        for _ in range(num_starting_tiles):
            self.spawn_tile()

    def spawn_tile(self):
        value = random.choices(self.spawn_values, weights=self.spawn_probs)
        return self.board.add_tile(value)

    def move(self, direction):
        if direction not in ['up', 'down', 'left', 'right']:
            raise Exception('Invalid move request')
        if direction == 'up':
            return self.board.shift_up() & self.spawn_tile()
        if direction == 'down':
            return self.board.shift_down() & self.spawn_tile()
        if direction == 'left':
            return self.board.shift_left() & self.spawn_tile()
        if direction == 'right':
            return self.board.shift_right() & self.spawn_tile()


if __name__ == '__main__':
    game = Game()
    print(game.board.tiles)
    while game.move('up'):
        print(game.board.tiles)