from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_cnt = 0
        rotten_oranges = deque()

        for i, row in enumerate(grid):
            for j, status in enumerate(row):
                if status == 1:
                    fresh_cnt += 1
                if status == 2:
                    rotten_oranges.append((i, j, 0))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        level = 0
        while rotten_oranges:
            x, y, level = rotten_oranges.popleft()
            for dir_x, dir_y in directions:
                next_x, next_y = x + dir_x, y + dir_y
                if not 0 <= next_x < m or not 0 <= next_y < n:
                    continue

                if grid[next_x][next_y] == 1:
                    fresh_cnt -= 1
                    grid[next_x][next_y] = 2
                    rotten_oranges.append((next_x, next_y, level + 1))

        if fresh_cnt > 0:
            return -1
        return level


def check_cases(s: Solution):
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert s.orangesRotting([[0, 2]]) == 0


def test_solution():
    check_cases(Solution())
