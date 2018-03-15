import unittest;
from infinite2DGrid import get_dimension, Infinite2DGridPart1, Infinite2DGridPart2;

class TestInfinite2DGrid(unittest.TestCase):

    def test_getDimension(self):
        self.assertEqual(get_dimension(1), 1);

    def test_getDimension2(self):
        self.assertEqual(get_dimension(3), 3);

    def test_getDimension3(self):
        self.assertEqual(get_dimension(13), 5);

    def test_getDimension4(self):
        self.assertEqual(get_dimension(1024), 33);

    def test_grid1_1(self):
        grid = Infinite2DGridPart1(1)
        grid.fill()
        self.assertEqual(grid.calculate_distance(), 0)

    def test_grid1_2(self):
        grid = Infinite2DGridPart1(12)
        grid.fill()
        self.assertEqual(grid.calculate_distance(), 3)

    def test_grid1_3(self):
        grid = Infinite2DGridPart1(23)
        grid.fill()
        self.assertEqual(grid.calculate_distance(), 2)

    def test_grid1_4(self):
        grid = Infinite2DGridPart1(1024)
        grid.fill()
        self.assertEqual(grid.calculate_distance(), 31)

    def test_grid2_1(self):
        grid = Infinite2DGridPart2(1)
        grid.fill()
        self.assertEqual(grid.get_last_value_written(), 1)

    def test_grid2_2(self):
        grid = Infinite2DGridPart2(2)
        grid.fill()
        self.assertEqual(grid.get_last_value_written(), 2)

    def test_grid2_3(self):
        grid = Infinite2DGridPart2(5)
        grid.fill()
        self.assertEqual(grid.get_last_value_written(), 5)

    def test_grid2_4(self):
        grid = Infinite2DGridPart2(6)
        grid.fill()
        self.assertEqual(grid.get_last_value_written(), 10)

    def test_grid2_5(self):
        grid = Infinite2DGridPart2(9)
        grid.fill()
        self.assertEqual(grid.get_last_value_written(), 10)


if __name__ == '__main__':
    unittest.main()
