import unittest
from typing import List, Tuple
from src.utils import dynamic_import
maze_solver = dynamic_import("maze_solver").maze_solver

Point = Tuple[int, int]

def draw_path(data: List[str], path: List[Point]) -> List[str]:
    data2 = [list(row) for row in data]
    for x, y in path:
        if 0 <= y < len(data2) and 0 <= x < len(data2[y]):
            data2[y][x] = '*'
    return [''.join(row) for row in data2]

class TestMazeSolver(unittest.TestCase):
    def test_maze_solver(self):
        maze = [
            "xxxxxxxxxx x",
            "x        x x",
            "x        x x",
            "x xxxxxxxx x",
            "x          x",
            "x xxxxxxxxxx",
        ]

        expected_result = [
            (10, 0),
            (10, 1),
            (10, 2),
            (10, 3),
            (10, 4),
            (9, 4),
            (8, 4),
            (7, 4),
            (6, 4),
            (5, 4),
            (4, 4),
            (3, 4),
            (2, 4),
            (1, 4),
            (1, 5),
        ]

        start = (10, 0)
        end = (1, 5)

        result = maze_solver(maze, 'x', start, end)
        self.assertEqual(draw_path(maze, result), draw_path(maze, expected_result))

if __name__ == '__main__':
    unittest.main()