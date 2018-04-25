import unittest;

from recursive_circus import RecursiveCircus;

class TestRecursiveCircus(unittest.TestCase):

    def test_parsing_file(self):
        circus = RecursiveCircus('./test_input.txt')
        root = circus.find_root()
        self.assertEqual('tknk', root.name)

if __name__ == '__main__':
    unittest.main()
