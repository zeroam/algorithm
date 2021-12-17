from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        queue = deque([(0, 0)])
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        # mark start with distance
        grid[0][0] = 1
        while queue:
            x, y = queue.popleft()
            if x == n - 1 and y == n - 1:
                return grid[x][y]

            for dir_x, dir_y in directions:
                next_x = x + dir_x
                next_y = y + dir_y
                if next_x < 0 or next_y < 0 or next_x >= n or next_y >= n:
                    continue

                if grid[next_x][next_y] == 0:
                    # set distance and add queue which is not visited
                    grid[next_x][next_y] = grid[x][y] + 1
                    queue.append((next_x, next_y))

        return -1


class SolutionVisited:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        directions = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        queue = deque([(0, 0, 1)])
        visited = set((0, 0))

        while queue:
            x, y, distance = queue.popleft()
            if x == n - 1 and y == n - 1:
                return distance

            for dir_x, dir_y in directions:
                next_x, next_y = x + dir_x, y + dir_y
                if not 0 <= next_x < n or not 0 <= next_y < n:
                    continue

                if grid[next_x][next_y] == 1 or (next_x, next_y) in visited:
                    continue

                visited.add((next_x, next_y))
                queue.append((next_x, next_y, distance + 1))

        return -1


def check_cases(s: Solution):
    s.shortestPathBinaryMatrix([[0, 1], [1, 0]]) == 2
    s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 0]]) == 4
    s.shortestPathBinaryMatrix([[1, 0, 0], [1, 1, 0], [1, 1, 0]]) == -1
    s.shortestPathBinaryMatrix([[0, 0, 0], [1, 1, 0], [1, 1, 1]]) == -1


def test_solution():
    check_cases(Solution())


def test_solution_visited():
    check_cases(SolutionVisited())
