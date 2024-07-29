import unittest
from src.utils import dynamic_import;

least_recently_used = dynamic_import("least_recently_used").least_recently_used



class LeastRecentlyUsedTest(unittest.TestCase):
    def test_last_recently_used(self):
        lru = least_recently_used(3); 
        
        self.assertEqual(lru.get("foo"), None)
        
        lru.update("foo", 69);     
        
        self.assertEqual(lru.get("foo"), 69)
        
        lru.update("bar", 420)
        self.assertEqual(lru.get("bar"), 420)

        lru.update("baz", 1337)
        self.assertEqual(lru.get("baz"), 1337)

        lru.update("ball", 69420)
        self.assertEqual(lru.get("ball"), 69420)
        self.assertEqual(lru.get("foo"), None)
        self.assertEqual(lru.get("bar"), 420)
        lru.update("foo", 69)
        self.assertEqual(lru.get("bar"), 420)
        self.assertEqual(lru.get("foo"), 69)