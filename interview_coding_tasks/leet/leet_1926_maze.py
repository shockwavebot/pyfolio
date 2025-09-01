"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') 
and walls (represented as '+'). You are also given the entrance of the maze, 
where entrance = [entrancerow, entrancecol] denotes the row and column 
of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. 
You cannot step into a cell with a wall, and you cannot step outside the maze. 
Your goal is to find the nearest exit from the entrance. 
An exit is defined as an empty cell that is at the border of the maze. 
The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance 
to the nearest exit, or -1 if no such path exists.
"""
from typing import List
from collections import deque


class GraphNode:
    def __init__(self, pos: List[int], came_from=None, depth=0):
        self.x = pos[0]
        self.y = pos[1]
        self.came_from: List[int] = came_from
        self.depth: int = depth


class Solution:
    def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
        # find a path -> DFS (LIFO, stack)
        # traversal graph, get min depth
        row_size = len(maze)
        col_size = len(maze[0])
        exit = 0
        root = GraphNode(entrance)
        stack = [root]
        while stack:
            current = stack.pop()
            # up
            if current.x > 0:
                x, y = current.x - 1, current.y
                if maze[x][y] == "." and current.came_from != [x, y]:
                    if x in [0, row_size - 1] or y in [0, col_size - 1]:
                        exit = min(exit, current.depth + 1) if exit else current.depth + 1
                    else:
                        stack.append(GraphNode([x, y], [current.x, current.y], current.depth + 1))
            # down
            if current.x < row_size -1:
                x, y = current.x + 1, current.y
                if maze[x][y] == "." and current.came_from != [x, y]:
                    if x in [0, row_size - 1] or y in [0, col_size - 1]:
                        exit = min(exit, current.depth + 1) if exit else current.depth + 1
                    else:
                        stack.append(GraphNode([x, y], [current.x, current.y], current.depth + 1))
            # left
            if current.y > 0:
                x ,y = current.x, current.y - 1
                if maze[x][y] == "." and current.came_from != [x, y]:
                    if x in [0, row_size - 1] or y in [0, col_size - 1]:
                        exit = min(exit, current.depth + 1) if exit else current.depth + 1
                    else:
                        stack.append(GraphNode([x, y], [current.x, current.y], current.depth + 1))
            #right 
            if current.y < col_size - 1:
                x, y = current.x, current.y + 1
                if maze[x][y] == "." and current.came_from != [x, y]:
                    if x in [0, row_size - 1] or y in [0, col_size - 1]:
                        exit = min(exit, current.depth + 1) if exit else current.depth + 1
                    else:
                        stack.append(GraphNode([x, y], [current.x, current.y], current.depth + 1))

        return exit if exit else -1

# BFS solution 
class Solution2:
    def nearestExit(maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        queue = deque([(entrance[0], entrance[1], 0)])  # (x, y, steps)
        visited = set([(entrance[0], entrance[1])])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            x, y, steps = queue.popleft()

            # check if it's an exit (but not the entrance)
            if (x, y) != (entrance[0], entrance[1]) and \
               (x == 0 or x == rows - 1 or y == 0 or y == cols - 1):
                return steps

            # explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == "." and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

        return -1

if __name__ == '__main__':
    maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    entrance = [1,2]
    assert Solution.nearestExit(maze, entrance) == 1
    maze = [[".","+"]]
    entrance = [0,0]
    assert Solution.nearestExit(maze, entrance) == -1
    maze = [
        [".","+","+","+","+"],
        [".","+",".",".","."],
        [".","+",".","+","."],
        [".",".",".","+","."],
        ["+","+","+","+","."]]
    entrance = [0,0]
    assert Solution.nearestExit(maze, entrance) == 1


