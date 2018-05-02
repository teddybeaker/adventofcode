import re
import unittest

from parser import FileParser


class Test(unittest.TestCase):

    def test_regex_condition(self):
        match = re.match(FileParser.condition_regex, 'c == 10')
        self.assertEqual('c', match.group(1))
        self.assertEqual('==', match.group(2))
        self.assertEqual('10', match.group(3))

    def test_regex_condition_negative(self):
        match = re.match(FileParser.condition_regex, 'bfx > -10')
        self.assertEqual('bfx', match.group(1))
        self.assertEqual('>', match.group(2))
        self.assertEqual('-10', match.group(3))

    def test_max_end_value(self):
        parser = FileParser('./test-input.txt')
        max_register_end_value = parser.get_max_register_end_value()
        self.assertEqual(None, max_register_end_value)

        parser.run()
        max_register_end_value = parser.get_max_register_end_value()
        self.assertEqual(1, max_register_end_value)

    def test_max_value(self):
        parser = FileParser('./test-input.txt')
        max_register_value = parser.get_max_register_value()
        self.assertEqual(0, max_register_value)

        parser.run()
        max_register_value = parser.get_max_register_value()
        self.assertEqual(10, max_register_value)


if __name__ == '__main__':
    unittest.main()