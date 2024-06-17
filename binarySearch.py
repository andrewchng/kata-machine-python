import unittest

def binary_search(haystack:list, needle:int) -> int:
    for item in haystack:
        if item == needle:
            return needle
    return -1

print(binary_search([1,2,3], 4))
    
class TestBinarySearch(unittest.TestCase):
    def test_found_element(self):
        self.assertEqual(binary_search([1, 2, 3], 2), 2)

    def test_not_found_element(self):
        self.assertEqual(binary_search([1, 2, 3], 4), -1)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 1), -1)

    def test_single_element_list(self):
        self.assertEqual(binary_search([42], 42), 42)
        self.assertEqual(binary_search([42], 10), -1)

if __name__ == '__main__':
    unittest.main()
