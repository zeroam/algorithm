from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        MAX_SIZE = 10000000000

        # make graph
        graph = [[MAX_SIZE] * n for _ in range(n)]
        for x, y, cost in times:
            graph[x - 1][y - 1] = cost

        start = k - 1
        visited = [False] * n
        costs = [MAX_SIZE] * n

        # start -> n
        costs[start] = 0

        cur_index = start
        for _ in range(n):
            # renew cost
            for neighbor, cost in enumerate(graph[cur_index]):
                if costs[cur_index] + cost < costs[neighbor]:
                    costs[neighbor] = costs[cur_index] + cost
            visited[cur_index] = True

            # find next_index
            next_index = -1
            max_value = MAX_SIZE
            for i in range(n):
                if visited[i]:
                    continue

                if graph[cur_index][i] <= max_value:
                    next_index = i

            cur_index = next_index

        print(costs)
        result = max(costs)
        return result if result != MAX_SIZE else -1


def check_cases(s: Solution):
    assert s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert s.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert s.networkDelayTime([[1, 2, 1]], 2, 2) == -1
    assert s.networkDelayTime([[1, 2, 1], [2, 3, 2]], 3, 1) == 3


def test_solution():
    check_cases(Solution())
