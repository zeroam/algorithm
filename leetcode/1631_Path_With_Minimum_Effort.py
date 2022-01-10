import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # make graph
        n = len(heights)
        directions = ((-1, 0), (0, 1), (-1, 0), (0, -1))

        graph = defaultdict(list)
        for i, row in enumerate(heights):
            for j, col in enumerate(row):
                for dir_row, dir_col in directions:
                    row_index = i + dir_row
                    col_index = j + dir_col

                    if not (0 <= row_index < n and 0 <= col_index < n):
                        continue

                    # up, right, down, left
                    graph[i, j].append((col, (row_index, col_index)))

        # initialize
        src = (0, 0)
        dest = (n - 1, n - 1)
        min_efforts = {}
        hq = [(0, src)]

        # iterate
        print(graph)
        while hq:
            cost, node = heapq.heappop(hq)
            if node in min_efforts:
                continue

            min_efforts[node] = cost
            for next_cost, next_node in graph[node]:
                min_efforts[next_node] = min_efforts[node] + next_cost
                heapq.heappush(hq, (min_efforts[next_node], next_node))

        print(min_efforts)
