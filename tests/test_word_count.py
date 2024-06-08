import unittest
from collections import Counter
from src.word_count import word_count
import os

class TestWordCount(unittest.TestCase):
    def test_word_count(self):
        result = word_count('tests/data/input.txt')
        expected_result = Counter({
            'this': 2,
            'is': 2,
            'a': 2,
            'test': 3,
            'only': 1,
        })
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
