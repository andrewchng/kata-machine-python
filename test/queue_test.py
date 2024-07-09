import unittest
from src.utils import dynamic_import

Queue = dynamic_import("queue").Queue

class TestQueue(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        q.enqueue(5)
        q.enqueue(10)
        q.enqueue(234)

        self.assertEqual(q.dequeue(), 5)

        q.enqueue(789)

        self.assertEqual(q.peek(), 10)
        self.assertEqual(q.length, 3)
        self.assertEqual(q.dequeue(), 10)
        self.assertEqual(q.length, 2)


if __name__ == '__main__':
    unittest.main()