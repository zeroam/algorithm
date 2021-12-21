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


class SolutionBFS:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # step1. build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        # Mark the round / level
        queue.append((-1, -1))

        # step2. start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
                continue

            for d in directions:
                neighbor_row, neighbor_col = row + d[0], col + d[1]
                if not 0 <= neighbor_row < ROWS or not 0 <= neighbor_col < COLS:
                    continue

                if grid[neighbor_row][neighbor_col] == 1:
                    grid[neighbor_row][neighbor_col] = 2
                    fresh_oranges -= 1
                    queue.append((neighbor_row, neighbor_col))

        return minutes_elapsed if fresh_oranges == 0 else -1


class SolutionInPlace:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def rotting_process(timestamp):
            to_be_continue = False
            for x in range(ROWS):
                for y in range(COLS):
                    if grid[x][y] != timestamp:
                        continue

                    for dir_x, dir_y in directions:
                        next_x, next_y = x + dir_x, y + dir_y
                        if not 0 <= next_x < ROWS or not 0 <= next_y < COLS:
                            continue

                        if grid[next_x][next_y] == 1:
                            grid[next_x][next_y] = timestamp + 1
                            to_be_continue = True

            return to_be_continue

        timestamp = 2
        while rotting_process(timestamp):
            timestamp += 1

        for row in grid:
            for state in row:
                if state == 1:
                    return -1

        return timestamp - 2


def check_cases(s: Solution):
    assert s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert s.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert s.orangesRotting([[0, 2]]) == 0


def test_solution():
    check_cases(Solution())


def test_solution_bfs():
    check_cases(SolutionBFS())


def test_solution_in_place_bfs():
    check_cases(SolutionInPlace())
