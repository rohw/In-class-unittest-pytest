import unittest
import word_count

class SimpleTest(unittst.TestCase):
    def test_word_count1(self):
        self.assertEqual(word_count.w_count(1234), "Input is not string")

    def test_word_count2(self):
        self.assertEqual(word_count.w_count("hi"), 1)

    def test_word_count3(self):
        self.assertEqual(word_count.w_count("Hi my name is Wonjun"), 5)

if __name__ == '__main__':
    unittest.main()