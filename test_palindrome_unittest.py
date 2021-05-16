import unittest
import palindrome

class SimpleTest(unittest.TestCase):
    def test_palindrome1(self):
        self.assertEqual(palindrome.palin(1234), "Input is not string")

    def test_palindrome2(self):
        self.assertEqual(palindrome.palin("1234"), False)

    def test_palindrome3(self):
        self.assertEqual(palindrome.palin("545"), True)

    def test_palindrome4(self):
        self.assertEqual(palindrome.palin("asdsa"), True)

if __name__ == '__main__':
    unittest.main()