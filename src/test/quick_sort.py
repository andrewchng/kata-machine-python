import unittest
from import_machine import dynamic_import

quick_sort = dynamic_import("quick_sort").quick_sort

class TestQuickSort(unittest.TestCase):
    def test_sort(self):
        arr = [9, 3, 7, 4, 69, 420, 42]
        quick_sort(arr)
        self.assertEqual(arr, [3, 4, 7, 9, 42, 69, 420])

if __name__ == "__main__":
    unittest.main()