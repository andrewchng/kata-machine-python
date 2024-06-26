import unittest
from src.utils import dynamic_import

Stack = dynamic_import("stack").Stack

class TestStack(unittest.TestCase):
    def test_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        stack.push(3)
        stack.push(4)
        stack.push(5)
        self.assertEqual(stack.peek(), 5)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), None)
        stack.push(7)
        self.assertEqual(stack.peek(), 7)

if __name__ == '__main__':
    unittest.main()