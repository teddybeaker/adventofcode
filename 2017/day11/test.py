import unittest
import math

from hex_ed_grid import HexEdGrid


class TestHexEd(unittest.TestCase):

    def test_tuple_addition(self):
        a = (0, 0, 0)
        b = (10, -5, 3)
        c = (a[0]+b[0], a[1]+b[1], a[2]+b[2])
        self.assertEqual(b, c)

    def test_distance(self):
        p = (1, 2, 3)
        sum = p[0]*p[0] + p[1]*p[1] + p[2]*p[2]
        result = math.sqrt(sum)
        self.assertEqual(14, sum)
        self.assertEqual(14**0.5, result)

    def test_example1(self):
        hex_ed = HexEdGrid('ne,ne,ne')
        result = hex_ed.process()
        self.assertEqual(3, result)

    def test_example2(self):
        hex_ed = HexEdGrid('ne,ne,sw,sw')
        result = hex_ed.process()
        self.assertEqual(0, result)
        self.assertEqual(2, hex_ed.max_distance())

    def test_example3(self):
        hex_ed = HexEdGrid('ne,ne,s,s')
        result = hex_ed.process()
        self.assertEqual(2, result)
        self.assertEqual(2, hex_ed.max_distance())

    def test_example4(self):
        hex_ed = HexEdGrid('se,sw,se,sw,sw')
        result = hex_ed.process()
        self.assertEqual(3, result)
        self.assertEqual(3, hex_ed.max_distance())


if __name__ == '__main__':
    unittest.main()
