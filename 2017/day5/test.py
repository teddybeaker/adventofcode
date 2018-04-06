import unittest;

from maze import Maze, StrangeMaze;

class TestMaze(unittest.TestCase):

    def test_empty(self):
        maze = Maze([])
        maze.get_out()
        self.assertEqual(0, maze.steps_needed())

    def test_sample(self):
        maze = Maze([0, 3, 0, 1, -3])
        maze.get_out()
        self.assertEqual(5, maze.steps_needed())

    def test_sample_strange(self):
        maze = StrangeMaze([0, 3, 0, 1, -3])
        maze.get_out()
        self.assertEqual(10, maze.steps_needed())


if __name__ == "__main__":
    unittest.main()
