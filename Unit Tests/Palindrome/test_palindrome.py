from palindrome import is_palindrome
import unittest

class TestPalindrome(unittest.TestCase):
    def test_true(self):
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("Racecar"))
        self.assertTrue(is_palindrome("maDam"))


    def test_false(self):
        self.assertFalse(is_palindrome("Hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("brother"))

if __name__ == "__main__":
    unittest.main()