import unittest

from knot_hash import KnotHash, part2

class KnotHashTest(unittest.TestCase):

    def test_init(self):
        kh = KnotHash(5)
        lst = kh.circular_list

        self.assertEqual(5, len(lst))
        self.assertEqual([0, 1, 2, 3, 4], lst)
        self.assertEqual(0, kh.current_position)
        self.assertEqual(0, kh.skip_size)

    def test_raises_exception_if_length_to_long(self):
        kh = KnotHash(5)
        self.assertRaises(Exception, kh.process, 6)

    def test_processing(self):
        kh = KnotHash(5)
        kh.process(3)
        self.assertEqual([2, 1, 0, 3, 4], kh.circular_list)
        self.assertEqual(3, kh.current_position)
        self.assertEqual(1, kh.skip_size)

        kh.process(4)
        self.assertEqual([4, 3, 0, 1, 2], kh.circular_list)
        self.assertEqual(3, kh.current_position)
        self.assertEqual(2, kh.skip_size)

        kh.process(1)
        self.assertEqual([4, 3, 0, 1, 2], kh.circular_list)
        self.assertEqual(1, kh.current_position)
        self.assertEqual(3, kh.skip_size)

        kh.process(5)
        self.assertEqual([3, 4, 2, 1, 0], kh.circular_list)
        self.assertEqual(4, kh.current_position)
        self.assertEqual(4, kh.skip_size)

    def test_whole(self):
        kh = KnotHash(5)
        for length in [3, 4, 1, 5]:
            kh.process(length)
        result = kh.circular_list[0]*kh.circular_list[1]
        self.assertEqual(12, result)

    def test_ascii_conversion(self):
        self.assertEqual(49, KnotHash.convert_to_ascii('1'))
        self.assertEqual(44, KnotHash.convert_to_ascii(','))
        self.assertEqual(50, KnotHash.convert_to_ascii('2'))
        self.assertEqual(51, KnotHash.convert_to_ascii('3'))

    def test_hex_conversion(self):
        self.assertEqual('40', KnotHash.conver_to_hex(64))
        self.assertEqual('07', KnotHash.conver_to_hex(7))
        self.assertEqual('ff', KnotHash.conver_to_hex(255))

    def x_test_multiple_runs(self):
        kh = KnotHash(10)
        for length in [49,44,50,44,51,17,31,73,47,23]:
            kh.process(length)
        self.assertEqual([3, 4, 1, 5, 17, 31, 73, 47, 23], kh.circular_list)

    def test_bitwise_xor(self):
        result = 65 ^ 27 ^ 9 ^ 1 ^ 4 ^ 3 ^ 40 ^ 50 ^ 91 ^ 7 ^ 6 ^ 0 ^ 2 ^ 5 ^ 68 ^ 22
        self.assertEqual(64, result)

        input = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
        self.assertEqual(64, KnotHash.bitwise_xor(input))

    def test_slice_list(self):
        input = [x for x in range(256)]
        slice = input[:16]
        self.assertEqual(16, len(slice))
        self.assertEqual(0, slice[0])
        self.assertEqual(15, slice[-1])

        self.assertEqual([0, 1, 2, 3], input[:4])
        self.assertEqual([4, 5, 6, 7], input[4:2*4])

    def test_example1(self):
        result = part2('')
        self.assertEqual('a2582a3a0e66e6e86e3812dcb672a272', result)

    def test_example2(self):
        result = part2('AoC 2017')
        self.assertEqual('33efeb34ea91902bb2f59c9920caa6cd', result)

    def test_example3(self):
        result = part2('1,2,3')
        self.assertEqual('3efbe78a8d82f29979031a4aa0b16a9d', result)

    def test_example4(self):
        result = part2('1,2,4')
        self.assertEqual('63960835bcdc130f0b66d7ff4f6a5a8e', result)



if __name__ == '__main__':
    unittest.main()
