from typing import List, Tuple

Point = Tuple[int, int]

def walk(maze:List[str], wall:str,  end:Point, curr:Point, visited: List[List[bool]], path: List[Point]):

    curX ,curY = curr

    if curX == end[0] and curY == end[1] :
        path.append(curr)
        return True
    if visited[curY][curX]:
        return False
    if maze[curY][curX] == wall :
        return False
    if curX < 0 or curY < 0 or curX >= len(maze[0]) or curY >= len(maze):
        return False
    
    path.append(curr)
    visited[curY][curX] = True

    dirs = [(1,0), (-1,0), (0,-1), (0,1)]
    for dx, dy in dirs :
        new_point = (curX+ dx, curY + dy)
        if(walk(maze, wall, end, new_point, visited, path)):
            return True
        
    path.pop()
    return False
    

def maze_solver(maze: List[str], wall: str, start:Point, end: Point) -> List[Point]:
    # visited = []
    # for i in range(len(maze)):
    #     visited.append([])
    #     for _ in range(len(maze[0])):
    #         visited[i].append(False)
    
    visited = [[False] * len(maze[0]) for i in range(len(maze))]

    path = []
    walk(maze, wall, end, start, visited, path)

    return path
