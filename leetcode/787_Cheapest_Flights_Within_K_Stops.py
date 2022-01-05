import heapq
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


class SolutionDijkstra:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # make graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # initialize
        hq = [(0, src, -1)]
        prices = [float('inf')] * n
        current_stops = [float('inf')] * n
        prices[src], current_stops[src] = 0, 0

        while hq:
            price, node, stop = heapq.heappop(hq)
            if node == dst:
                return price

            # update price
            prices[node] = price

            if stop + 1 > k:
                continue

            # heappush
            for next_node, next_price in graph[node]:
                if price + next_price < prices[next_node]:
                    prices[next_node] = price + next_price
                    heapq.heappush(hq, (price + next_price, next_node, stop + 1))
                elif stop < current_stops[next_node]:
                    heapq.heappush(hq, (price + next_price, next_node, stop + 1))

                current_stops[next_node] = stop

        return prices[dst] if prices[dst] != float('inf') else -1


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

    n = 4
    flights = [[0,1,1],[0,2,5],[1,2,1],[2,3,1]]
    src = 0
    dst = 3
    k = 1
    assert s.findCheapestPrice(n, flights, src, dst, k) == 6

    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    assert s.findCheapestPrice(n, flights, src, dst, k) == 200


def test_solution():
    check_cases(Solution())


def test_solution_dijkstra():
    check_cases(SolutionDijkstra())
