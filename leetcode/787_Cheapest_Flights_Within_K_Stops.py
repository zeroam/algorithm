import heapq
from collections import defaultdict, deque
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


class SolutionDFS:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[u].append((v, price))

        prices = {}

        def traverse(node, stop):
            if node == dst:
                return 0

            if stop == k + 1:
                return float('inf')

            if (node, stop) in prices:
                return prices[(node, stop)]

            ans = float('inf')
            for next_node, next_price in graph[node]:
                ans = min(ans, traverse(next_node, stop + 1) + next_price)

            prices[(node, stop)] = ans
            return ans

        ans = traverse(src, 0)
        return ans if ans != float('inf') else -1


class SolutionBellmanFord:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, price in flights:
            graph[v].append((u, price))


        # bellman ford algorithm
        cur_routes = [float('inf')] * n
        cur_routes[src] = 0

        for _ in range(k + 1):
            # iterate from prev_routes
            prev_routes = cur_routes.copy()

            for u, v, price in flights:
                cur_routes[v] = min(cur_routes[v], prev_routes[u] + price)

        ans = cur_routes[dst]
        return ans if ans != float('inf') else -1


class SolutionBFS:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj_matrix = [[0] * n for _ in range(n)]
        for u, v, w in flights:
            adj_matrix[u][v] = w

        distances = {}
        distances[(src, 0)] = 0

        queue = deque([src])

        stops = 0
        ans = float('inf')

        while queue and stops < k + 1:
            for _ in range(len(queue)):
                node = queue.popleft()

                for nei in range(n):
                    if adj_matrix[node][nei] == 0:
                        continue

                    d_u = distances.get((node, stops), float('inf'))
                    d_v = distances.get((nei, stops + 1), float('inf'))
                    w_uv = adj_matrix[node][nei]

                    if stops == k and nei != dst:
                        continue

                    if d_u + w_uv < d_v:
                        distances[(nei, stops + 1)] = d_u + w_uv
                        queue.append(nei)

                        if nei == dst:
                            ans = min(ans, d_u + w_uv)

            stops += 1

        return ans if ans != float('inf') else -1


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


def test_solution_dfs():
    check_cases(SolutionDFS())


def test_solution_bellman_ford():
    check_cases(SolutionBellmanFord())


def test_solution_bfs():
    check_cases(SolutionBFS())
