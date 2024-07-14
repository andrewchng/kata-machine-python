import unittest
from src.utils import dynamic_import
singly_linked_list = dynamic_import("singly_linked_list").singly_linked_list

class TestSingleLinkedList(unittest.TestCase):
    def test_single_linked_list(self):
        list =  singly_linked_list()
        list.append(5)
        list.append(7)
        list.append(9)

        self.assertEqual(list.get(2),9)
        self.assertEqual(list.remove_at(1),7)

        # [5, 9]
        self.assertEqual(list.length,2)

        list.append(11)

        # [5, 9, 11]

        self.assertEqual(list.remove_at(1),9)

        # [5, 11]

        self.assertEqual(list.remove(9), None)
        self.assertEqual(list.remove_at(0),5)

        # [11]

        self.assertEqual(list.remove_at(0),11)

        # []

        self.assertEqual(list.length,0)

        list.prepend(5)
        list.prepend(7)
        list.prepend(9)

        #[9, 7 ,5]

        self.assertEqual(list.get(2),5)
        self.assertEqual(list.get(0),9)
        self.assertEqual(list.remove(9),9)
        self.assertEqual(list.length,2)
        self.assertEqual(list.get(0),7)

       
if __name__ == '__main__':
    unittest.main()