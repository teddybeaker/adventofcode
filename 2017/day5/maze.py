class Maze:

    def __init__(self, offsets):
        self._offsets = offsets;
        self._steps_needed = 0;
        self._current_position = 0;

    def steps_needed(self):
        return self._steps_needed;

    def get_out(self):
        if len(self._offsets) < 1:
            return;
        while self._current_position < len(self._offsets):
            current_offset = self._offsets[self._current_position]
            self._update_offset()
            self._current_position += current_offset
            self._steps_needed += 1
            #print (self._offsets)

    def _update_offset(self):
        self._offsets[self._current_position] += 1


class StrangeMaze(Maze):

    def _update_offset(self):
        if self._offsets[self._current_position] >= 3:
            self._offsets[self._current_position] -= 1
        else:
            self._offsets[self._current_position] += 1


if __name__ == "__main__":
    with open("./input.txt") as f:
        content = f.read()
        offsets = []
        for value in content.split("\n"):
            if len(value.strip()) > 0:
                offsets.append(int(value))
        maze = Maze(offsets[:])
        maze.get_out()
        print("needed %d steps to get out" % maze.steps_needed())

        strange_maze = StrangeMaze(offsets[:])
        strange_maze.get_out()
        print("needed %d steps to get out of strange maze" % strange_maze.steps_needed())
    f.closed
