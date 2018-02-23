import unittest
from sum_duplicates import sibling_duplicates, halfway_around_duplicates;

class TestStringMethods(unittest.TestCase):

    def test_sibling1(self):
        result = sibling_duplicates('1122')
        self.assertEqual(result, 3)

    def test_sibling2(self):
        result = sibling_duplicates('1234')
        self.assertEqual(result, 0)

    def test_sibling3(self):
        result = sibling_duplicates('91212129')
        self.assertEqual(result, 9)

    def test_halfway_around1(self):
        result = halfway_around_duplicates('1212')
        self.assertEqual(result, 6)

    def test_halfway_around2(self):
        result = halfway_around_duplicates('1221')
        self.assertEqual(result, 0)

    def test_halfway_around3(self):
        result = halfway_around_duplicates('123425')
        self.assertEqual(result, 4)

    def test_halfway_around4(self):
        result = halfway_around_duplicates('123123')
        self.assertEqual(result, 12)

    def test_halfway_around5(self):
        result = halfway_around_duplicates('12131415')
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
