import unittest
from src.utils import dynamic_import
binary_search = dynamic_import("binary_search").binary_search

class TestBinarySearch(unittest.TestCase):
    def test_found_element(self):
        self.assertEqual(binary_search([1, 2, 3], 2), True)

    def test_not_found_element(self):
        self.assertEqual(binary_search([1, 2, 3], 4), False)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), False)

    def test_single_element_list(self):
        self.assertEqual(binary_search([42], 42), True)
        self.assertEqual(binary_search([42], 10), False)

if __name__ == '__main__':
    unittest.main()