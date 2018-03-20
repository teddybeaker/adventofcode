import unittest;
from check_passphrase import is_valid_passphrase, is_valid_passphrase_strict, is_anagram, is_valid_passphrase_strict2;

class TestPassPhraseChecker(unittest.TestCase):

    def test_1_1(self):
        result = is_valid_passphrase("aa bb cc dd ee")
        self.assertTrue(result)

    def test_1_2(self):
        result = is_valid_passphrase("aa bb cc dd aa")
        self.assertFalse(result)

    def test_1_3(self):
        result = is_valid_passphrase("aa bb cc dd aaa")
        self.assertTrue(result)

    def test_2_1(self):
        result = is_valid_passphrase_strict("abcde fghij")
        self.assertTrue(result)

    def test_2_2(self):
        result = is_valid_passphrase_strict("abcde xyz ecdab")
        self.assertFalse(result)

    def test_2_3(self):
        result = is_valid_passphrase_strict("a ab abc abd abf abj")
        self.assertTrue(result)

    def test_2_4(self):
        result = is_valid_passphrase_strict("iiii oiii ooii oooi oooo")
        self.assertTrue(result)

    def test_2_5(self):
        result = is_valid_passphrase_strict("oiii ioii iioi iiio")
        self.assertFalse(result)

    def test_3_1(self):
        self.assertTrue(is_anagram("abcde", "abcde"))

    def test_3_2(self):
        self.assertTrue(is_anagram("abcde", "ecdab"))

    def test_3_3(self):
        self.assertFalse(is_anagram("abcde", "fghij"))

    def test_4_1(self):
        result = is_valid_passphrase_strict2("abcde fghij")
        self.assertTrue(result)

    def test_4_2(self):
        result = is_valid_passphrase_strict2("abcde xyz ecdab")
        self.assertFalse(result)

    def test_4_3(self):
        result = is_valid_passphrase_strict2("a ab abc abd abf abj")
        self.assertTrue(result)

    def test_4_4(self):
        result = is_valid_passphrase_strict2("iiii oiii ooii oooi oooo")
        self.assertTrue(result)

    def test_4_5(self):
        result = is_valid_passphrase_strict2("oiii ioii iioi iiio")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
