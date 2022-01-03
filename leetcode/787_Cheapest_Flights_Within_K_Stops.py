from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[v].append((u, w))

        # make table
        price_table = [[float('inf')] * n for _ in range(k + 2)]
        for i in range(k + 1):
            price_table[i][src] = 0

        for edge in range(1, k + 2):
            for dst_node in range(n):
                for src_node, price in graph[dst_node]:
                    price_table[edge][dst_node] = min(price_table[edge][dst_node], price_table[edge -1][src_node] + price)

        return price_table[k + 1][dst] if price_table[k + 1][dst] < float('inf') else -1


def check_cases(s: Solution):
    n = 5
    flights = [[1,2,10],[2,0,7],[1,3,8],[4,0,10],[3,4,2],[4,2,10],[0,3,3],[3,1,6],[2,4,5]]
    src = 0
    dst = 4
    k = 1
    assert s.findCheapestPrice(n, flights, src, dst, k) == 5

    n = 3
    flights = [[0,1,2],[1,2,1],[2,0,10]]
    src = 1
    dst = 2
    k = 1
    assert s.findCheapestPrice(n, flights, src, dst, k) == 1


def test_solution():
    check_cases(Solution())
