import unittest;
from infinite2DGrid import get_dimension, Infinite2DGrid;

class TestInfinite2DGrid(unittest.TestCase):

    def test_getDimension(self):
        self.assertEqual(get_dimension(1), 1);

    def test_getDimension2(self):
        self.assertEqual(get_dimension(3), 3);

    def test_getDimension3(self):
        self.assertEqual(get_dimension(13), 5);

    def test_getDimension4(self):
        self.assertEqual(get_dimension(1024), 33);

    def test_grid1(self):
        grid = Infinite2DGrid(1)
        grid.fill()
        self.assertEqual(grid.calculate_distance(), 0)

    def test_grid2(self):
        grid = Infinite2DGrid(12)
        grid.fill()
        self.assertEqual(grid.calculate_distance(), 3)

    def test_grid3(self):
        grid = Infinite2DGrid(23)
        grid.fill()
        self.assertEqual(grid.calculate_distance(), 2)

    def test_grid4(self):
        grid = Infinite2DGrid(1024)
        grid.fill()
        self.assertEqual(grid.calculate_distance(), 31)


if __name__ == '__main__':
    unittest.main()
