import unittest

from digital_plumber import DigitalPlumber;

class DigitalPlumberTest(unittest.TestCase):

    def test_parsing(self):
        dp = DigitalPlumber('test-input.txt')
        dp.parse()
        groups = dp.process()
        self.assertEqual(2, len(groups))
        group = groups['0']
        self.assertEqual(6, len(group))
        self.assertTrue('0' in group)
        self.assertTrue('2' in group)
        self.assertTrue('3' in group)
        self.assertTrue('4' in group)
        self.assertTrue('5' in group)
        self.assertTrue('6' in group)
        self.assertFalse('1' in group)

        group1 = groups['1']
        self.assertEqual(1, len(group1))
        self.assertTrue('1' in group1)

    def test_smoke_set(self):
        s = set([1,2,1,3])
        self.assertEqual(3, len(s))
        s.add(4)
        s.add(2)
        self.assertEqual(4, len(s))

    def test_smoke_dict(self):
        d = {'0': 'foo', '1': 'bar', '2': 'foobar'}
        for key in d:
            self.assertEqual('0', key)
            break


if __name__ == '__main__':
    unittest.main()
