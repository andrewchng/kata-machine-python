import unittest
from src.utils import dynamic_import

bubble_sort = dynamic_import('bubble_sort').bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [6,1,4,2,5,3,9]
        bubble_sort(arr)
        self.assertEqual(arr, [1,2,3,4,5,6,9])

if __name__ == '__main__':
    unittest.main()