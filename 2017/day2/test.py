import unittest
from checksum import checksum_row_minmax, checksum_row_evenly_divisible, checksum_matrix


class TestChecksumCalculation(unittest.TestCase):

    def test_checksum_row_minmax1(self):
        row = [5, 1, 9, 5]
        result = checksum_row_minmax(row)
        self.assertEqual(result, 8)

    def test_2(self):
        row = [7, 5, 3]
        result = checksum_row_minmax(row)
        self.assertEqual(result, 4)

    def test_checksum_row_minmax3(self):
        row = [2, 4, 6, 8]
        result = checksum_row_minmax(row)
        self.assertEqual(result, 6)

    def test_checksum_row_evenly_divisable1(self):
        row = [5, 9, 2, 8]
        result = checksum_row_evenly_divisible(row)
        self.assertEqual(result, 4)

    def test_checksum_row_evenly_divisable2(self):
        row = [9, 4, 7, 3]
        result = checksum_row_evenly_divisible(row)
        self.assertEqual(result, 3)

    def test_checksum_row_evenly_divisable3(self):
        row = [3, 8, 6, 5]
        result = checksum_row_evenly_divisible(row)
        self.assertEqual(result, 2)

    def test_checksum_row_evenly_divisable_exception(self):
        self.assertRaises(Exception, checksum_row_evenly_divisible, [1])
        self.assertRaises(Exception, checksum_row_evenly_divisible, [2, 3, 5, 7])

    def test_checksum_matrix(self):
        matrix = [
            [5, 1, 9, 5],
            [7, 5, 3],
            [2, 4, 6, 8]
        ]
        result = checksum_matrix(matrix, checksum_row_minmax)
        self.assertEqual(result, 18)

    def test_checksum_matrix2(self):
        matrix = [
            [5, 9, 2, 8],
            [9, 4, 7, 3],
            [3, 8, 6, 5]
        ]
        result = checksum_matrix(matrix, checksum_row_evenly_divisible)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
