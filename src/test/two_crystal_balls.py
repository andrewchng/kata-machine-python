import unittest
from src.utils import dynamic_import

two_crystal_balls = dynamic_import("two_crystal_balls").two_crystal_balls

class test_two_crystal_balls(unittest.TestCase):
    def test_two_cystal_balls(self):
        arr = [False, False,False,False,False,False,False,True,True,True,True,True,]
        self.assertEqual(two_crystal_balls(arr), 7)
    
    def test_two_cystal_balls_nil(self):
        arr = [False, False,False,False,False,False,False]
        self.assertEqual(two_crystal_balls(arr), -1)



