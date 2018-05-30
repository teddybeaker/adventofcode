# solved with the help of https://github.com/jcpuja/advent-of-code-python/blob/master/day11/task01.py
import math


class HexEdGrid:

    moves = {
        'n': (0, 1, -1),
        'ne': (1, 0, -1),
        'se': (1, -1, 0),
        's': (0, -1, 1),
        'sw': (-1, 0, 1),
        'nw': (-1, 1, 0)
    }

    def __init__(self, input):
        self._input = input.split(',')
        self._position = self._origin = (0, 0, 0)

    def process(self):
        for step in self._input:
            move = self.moves[step]
            self._position = (self._position[0] + move[0], self._position[1] + move[1], self._position[2] + move[2])
        print("after run, position is %s, %s, %s" % self._position)
        return self._distance_to_origin()

    def _distance_to_origin(self):
        return max(abs(self._position[0] - self._origin[0]), abs(self._position[1] - self._origin[1]), abs(self._position[2] - self._origin[2]))


if __name__ == '__main__':
    with open('./input.txt') as f:
        content = f.read().strip()
        hex_ed = HexEdGrid(content)
        steps = hex_ed.process()
        print("steps needed %s" % steps)
