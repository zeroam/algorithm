import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # initialize
        m, n = len(heights), len(heights[0])
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))

        src = (0, 0)
        dest = (m - 1, n - 1)
        min_efforts = {}
        hq = [(0, 0, 0)]

        # iterate
        max_effort = 0
        while hq:
            effort, cur_row, cur_col = heapq.heappop(hq)
            node = (cur_row, cur_col)
            if node in min_efforts:
                continue

            if effort > max_effort:
                max_effort = effort

            if node == dest:
                break

            min_efforts[node] = effort

            cur_height = heights[cur_row][cur_col]
            for dir_row, dir_col in directions:
                next_row = cur_row + dir_row
                next_col = cur_col + dir_col

                if 0 <= next_row < m and 0 <= next_col < n:
                    next_height = heights[next_row][next_col]
                    heapq.heappush(hq, (abs(cur_height - next_height), next_row, next_col))

        return max_effort


class SolutionBruteForceDFS:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # initialize
        m, n = len(heights), len(heights[0])
        visited = set()

        self.max_so_far = float('inf')
        def dfs(x: int, y: int, max_diff: int):
            if (x, y) == (m - 1, n - 1):
                self.max_so_far = min(self.max_so_far, max_diff)
                return max_diff

            cur_height = heights[x][y]
            min_effort = float('inf')
            visited.add((x, y))
            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                adj_x = x + dx
                adj_y = y + dy

                if (adj_x, adj_y) in visited:
                    continue
                if not (0 <= adj_x < m and 0 <= adj_y < n):
                    continue

                cur_diff = abs(heights[adj_x][adj_y] - cur_height)
                max_cur_diff = max(max_diff, cur_diff)
                if max_cur_diff > self.max_so_far:  # backtracking
                    continue

                result = dfs(adj_x, adj_y, max_cur_diff)
                min_effort = min(min_effort, result)
            visited.remove((x, y))

            return min_effort

        return dfs(0, 0, 0)


class SolutionDijkstra:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # initialize
        m, n = len(heights), len(heights[0])

        diff_matrix = [[float('inf')] * n for _ in range(m)]
        diff_matrix[0][0] = 0
        visited = [[False] * n for _ in range(m)]
        hq = [(0, 0, 0)]

        while hq:
            cur_diff, x, y = heapq.heappop(hq)
            visited[x][y] = True

            cur_height = heights[x][y]
            for dx,dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                nei_x = x + dx
                nei_y = y + dy

                if not (0 <= nei_x < m and 0 <= nei_y < n):
                    continue
                if visited[nei_x][nei_y]:
                    continue

                nei_diff = abs(heights[nei_x][nei_y] - cur_height)
                max_diff = max(cur_diff, nei_diff)
                if diff_matrix[nei_x][nei_y] > max_diff:
                    diff_matrix[nei_x][nei_y] = max_diff
                    heapq.heappush(hq, (max_diff, nei_x, nei_y))

        return diff_matrix[-1][-1]


class SolutionDisjointJoin:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        pass


def check_cases(s: Solution):
    assert s.minimumEffortPath([[3]]) == 0
    assert s.minimumEffortPath([[1, 10, 6, 7, 9, 10, 4, 9]]) == 9
    assert s.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert s.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0


def test_solution():
    check_cases(Solution())


def test_solution_bruteforce_dfs():
    check_cases(SolutionBruteForceDFS())


def test_solution_dijkstra():
    check_cases(SolutionDijkstra())


def test_solution_disjoint_join():
    check_cases(SolutionDisjointJoin())
