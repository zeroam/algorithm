import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # make graph
        graph = defaultdict(list)
        for x, y, cost in times:
            graph[x - 1].append((y - 1, cost))

        visited = [False] * n
        costs = [float('inf')] * n
        costs[k - 1] = 0

        # traverse and update cost
        while True:
            # find cand_node
            cand_node = -1
            cand_dist = float('inf')
            for i in range(n):
                if visited[i]:
                    continue

                if costs[i] < cand_dist:
                    cand_node = i
                    cand_dist = costs[i]

            if cand_node == -1:
                break

            # update costs
            visited[cand_node] = True
            for node, cost in graph[cand_node]:
                costs[node] = min(costs[node], costs[cand_node] + cost)

        max_cost = max(costs)
        return max_cost if max_cost < float('inf') else -1


class SolutionPriorityQueue:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # make graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # initialize
        pq = [(0, k)]
        dist = {}

        while pq:
            # find min node
            d, node = heapq.heappop(pq)
            if node in dist:
                continue

            # update routing costs
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei in dist:
                    continue

                heapq.heappush(pq, (d + d2, nei))

        return max(dist.values()) if len(dist) == n else -1


def check_cases(s: Solution):
    assert s.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert s.networkDelayTime([[1, 2, 1]], 2, 1) == 1
    assert s.networkDelayTime([[1, 2, 1]], 2, 2) == -1
    assert s.networkDelayTime([[1, 2, 1], [2, 3, 2]], 3, 1) == 3
    assert s.networkDelayTime([[1, 2, 1], [1, 3, 1], [1, 4, 3], [2, 4, 1], [3, 5, 1], [4, 5, 2]], 5, 1) == 2


def test_solution():
    check_cases(Solution())


def test_solution_priority_queue():
    check_cases(SolutionPriorityQueue())
