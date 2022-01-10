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


def check_cases(s: Solution):
    assert s.minimumEffortPath([[3]]) == 0
    assert s.minimumEffortPath([[1, 10, 6, 7, 9, 10, 4, 9]]) == 9
    assert s.minimumEffortPath([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert s.minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert s.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]) == 0


def test_solution():
    check_cases(Solution())
