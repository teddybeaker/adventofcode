import unittest;

from recursive_circus import RecursiveCircus;

class TestRecursiveCircus(unittest.TestCase):

    def test_find_root(self):
        circus = RecursiveCircus('./test_input.txt')
        root = circus.find_root()
        self.assertEqual('tknk', root.name)

    def test_find_last_unbalanced(self):
        circus = RecursiveCircus('./test_input.txt')
        unbalanced = circus.find_unbalanced()
        self.assertIsNotNone(unbalanced)
        self.assertEqual('tknk', unbalanced.name)
        self.assertFalse(unbalanced.is_balanced())

    def test_find_new_weight(self):
        circus = RecursiveCircus('./test_input.txt')
        (candidate, new_weight) = circus.find_new_weight()
        self.assertIsNotNone(candidate)
        self.assertEqual('ugml', candidate.name)
        self.assertEqual(60, new_weight)

if __name__ == '__main__':
    unittest.main()
