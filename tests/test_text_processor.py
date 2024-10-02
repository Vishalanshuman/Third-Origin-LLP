import unittest
from src.text_processor import count_words, count_characters, count_lines, find_word

class TestTextProcessor(unittest.TestCase):

    def test_count_words(self):
        self.assertEqual(count_words('sample.txt'), 619)  

    def test_count_characters(self):
        self.assertEqual(count_characters('sample.txt'), 4165)  

    def test_count_lines(self):
        self.assertEqual(count_lines('sample.txt'), 3104)  

    def test_find_word(self):
        self.assertEqual(find_word('sample.txt', 'example'), 2)  

if __name__ == '__main__':
    unittest.main()
