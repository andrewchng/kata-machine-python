import unittest
from import_machine import dynamic_import
linear_search = dynamic_import("linear_search").linear_search

class TestBinarySearch(unittest.TestCase):
    def test_found_element(self):
        self.assertEqual(linear_search([1, 2, 3], 2), True)

    def test_not_found_element(self):
        self.assertEqual(linear_search([1, 2, 3], 4), False)

    def test_empty_list(self):
        self.assertEqual(linear_search([], 1), False)

    def test_single_element_list(self):
        self.assertEqual(linear_search([42], 42), True)
        self.assertEqual(linear_search([42], 10), False)

if __name__ == '__main__':
    unittest.main()