import math
from abc import ABC, abstractmethod

# solved with the help of
# https://github.com/jcpuja/advent-of-code-python/blob/master/day03/task01.py
# look there for nicely commented code

class Infinite2DGrid(ABC):

    directions = ['right', 'up', 'left', 'down']

    def __init__(self, dimension):
        self._dimension = dimension
        self._grid = [[0 for x in range(self._dimension)] for y in range(self._dimension)]
        origin = math.floor(self._dimension / 2)
        self._origin = self._coordinate = (origin, origin)

    def _init_fields(self):
        self._current_dimension = 1
        self._items_filled_on_side = 0
        self._sides_filled = 3
        self._current_direction = self.directions[0]

    def fill(self):
        self._init_fields()
        for i in range(1, self._dimension**2+1):
            value = self._calculate_value(i)
            self._set_value(value)
            self._increment_items_filled()

            if (self._stop(value)): break

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

    @abstractmethod
    def _stop(self, value):
        pass

    @abstractmethod
    def _calculate_value(self, step):
        pass

    def print(self):
        for row in self._grid:
            print(row)


class Infinite2DGridPart1(Infinite2DGrid):

    def __init__(self, max_value):
        super().__init__(get_dimension(max_value))
        self._max_value = max_value

    def _stop(self, value):
        return value >= self._max_value

    def _calculate_value(self, step):
        return step

    def calculate_distance(self):
        return self._manhattan_distance(self._origin, self._coordinate)

    def _manhattan_distance(self, coord1, coord2):
        return abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])


class Infinite2DGridPart2(Infinite2DGrid):

    def __init__(self, max_value):
        super().__init__(get_dimension(max_value)+4)
        self._max_value = max_value
        self._last_value = 1

    def _stop(self, value):
        return value >= self._max_value

    def _calculate_value(self, step):
        if (self._coordinate == self._origin):
            return 1
        sum = 0
        x, y = self._coordinate
        for i in range(-1, 2):
            for j in range(-1, 2):
                sum += self._grid[x+i][y+j]
        self._last_value = sum
        return sum

    def get_last_value_written(self):
        return self._last_value


def get_dimension(number):
    dimension = math.ceil(math.sqrt(number))
    if dimension % 2 == 0:
        dimension += 1;
    return dimension


if __name__ == '__main__':
    input = 361527
    print('the grid size is %d' % get_dimension(input))
    grid1 = Infinite2DGridPart1(input)
    grid1.fill()
    #grid1.print()
    print('the distance is %d ' % grid1.calculate_distance())

    grid2 = Infinite2DGridPart2(input)
    grid2.fill()
    #grid2.print()
    print('the first value written greater than %d is %d ' % (input, grid2.get_last_value_written()))
