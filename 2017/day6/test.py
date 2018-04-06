import unittest;

from reallocator import Reallocator;

class TestReallocator(unittest.TestCase):

    def test_cycle(self):
        testee = Reallocator([0, 2, 7, 0])
        testee.run()
        self.assertEqual(5, testee.get_cycles())

    def test_loop(self):
        testee = Reallocator([0, 2, 7, 0])
        testee.run()
        self.assertEqual(4, testee.get_loop_size())

if __name__ == '__main__':
    unittest.main()
