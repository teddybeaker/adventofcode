import unittest

from know_hash import KnowHash

class KnowHashTest(unittest.TestCase):

    def test_init(self):
        kh = KnowHash(5)
        lst = kh.circular_list

        self.assertEqual(5, len(lst))
        self.assertEqual([0, 1, 2, 3, 4], lst)
        self.assertEqual(0, kh.current_position)
        self.assertEqual(0, kh.skip_size)

    def test_raises_exception_if_length_to_long(self):
        kh = KnowHash(5)
        self.assertRaises(Exception, kh.process, 6)

    def test_processing(self):
        kh = KnowHash(5)
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
        kh = KnowHash(5)
        for length in [3, 4, 1, 5]:
            kh.process(length)
        result = kh.circular_list[0]*kh.circular_list[1]
        self.assertEqual(12, result)



if __name__ == '__main__':
    unittest.main()
