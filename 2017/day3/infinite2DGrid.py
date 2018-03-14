import math;

# solved with the help of
# https://github.com/jcpuja/advent-of-code-python/blob/master/day03/task01.py
# look there for nicely commented code

class Infinite2DGrid:

    directions = ['right', 'up', 'left', 'down']

    def __init__(self, number):
        self._max_value = number
        dimension = get_dimension(number)
        self._grid = [[0 for x in range(dimension)] for y in range(dimension)]
        origin = math.floor(dimension / 2)
        self._origin = self._coordinate = (origin, origin)

    def _init_fields(self):
        self._current_dimension = 1
        self._items_filled_on_side = 0
        self._sides_filled = 3
        self._current_direction = self.directions[0]

    def fill(self):
        self._init_fields()
        for x in range(1, self._max_value):
            self._set_value(x)
            self._increment_items_filled()

            if self._has_finished_side():
                self._increment_sides_filled()

                if not self._on_last_side():
                    self._change_direction()
                    self._reset_items_filled()

                    if self._after_last_side():
                        self._reset_sides_filled()
                        self._increment_dimension()

            self._move_to_next()

    def _set_value(self, value):
        self._grid[self._coordinate[0]][self._coordinate[1]] = value

    def _increment_items_filled(self):
        self._items_filled_on_side += 1

    def _reset_items_filled(self):
        self._items_filled_on_side = 1

    def _increment_sides_filled(self):
        self._sides_filled += 1

    def _reset_sides_filled(self):
        self._sides_filled = 0
        self._items_filled_on_side = 2

    def _has_finished_side(self):
        return self._items_filled_on_side >= self._current_dimension

    def _has_finished_circle(self):
        return self._current_direction == "right"

    def _on_last_side(self):
        return self._sides_filled == 4

    def _after_last_side(self):
        return self._sides_filled == 5

    def _change_direction(self):
        index = self.directions.index(self._current_direction)
        self._current_direction = self.directions[(index + 1) % len(self.directions)]
        self._items_filled_on_side = 0

    def _increment_dimension(self):
        self._current_dimension += 2

    def _move_to_next(self):
        if self._current_direction == 'right':
            self._coordinate = (self._coordinate[0], self._coordinate[1]+1)
        elif self._current_direction == 'up':
            self._coordinate = (self._coordinate[0]-1, self._coordinate[1])
        elif self._current_direction == 'left':
            self._coordinate = (self._coordinate[0], self._coordinate[1]-1)
        elif self._current_direction == 'down':
            self._coordinate = (self._coordinate[0]+1, self._coordinate[1])
        else:
            raise ValueError("can't handle direction %s " % s)

    def calculate_distance(self):
        return self._manhattan_distance(self._origin, self._coordinate)

    def _manhattan_distance(self, coord1, coord2):
        return abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])

    def print(self):
        for row in self._grid:
            print(row)


def get_dimension(number):
    dimension = math.ceil(math.sqrt(number))
    if dimension % 2 == 0:
        dimension += 1;
    return dimension


if __name__ == '__main__':
    input = 361527
    print('the grid size is %d' % get_dimension(input))
    grid = Infinite2DGrid(input)
    grid.fill()
    #grid.print()
    print('the distance is %d ' % grid.calculate_distance())
