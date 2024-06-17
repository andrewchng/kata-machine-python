import unittest
from src.linear_search import linear_search

class TestBinarySearch(unittest.TestCase):
    def test_found_element(self):
        self.assertEqual(linear_search([1, 2, 3], 2), 2)

    def test_not_found_element(self):
        self.assertEqual(linear_search([1, 2, 3], 4), -1)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), -1)

    def test_single_element_list(self):
        self.assertEqual(linear_search([42], 42), 42)
        self.assertEqual(linear_search([42], 10), -1)

if __name__ == '__main__':
    unittest.main()