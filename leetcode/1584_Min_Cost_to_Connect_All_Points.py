import heapq
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.root = [x for x in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        size = len(points)

        # make distances between points
        distances = []
        for i in range(size):
            for j in range(i + 1, size):
                point1 = points[i]
                point2 = points[j]
                distance = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

                distances.append((i, j, distance))

        # sort by distance
        distances.sort(key=lambda x: x[2])

        # disjoint join
        connected = 0
        value = 0
        uf = UnionFind(size)

        for i, j, distance in distances:
            if uf.is_connected(i, j):
                continue

            uf.union(i, j)
            connected += 1
            value += distance

            if connected == size - 1:
                break

        return value


class SolutionKruskal:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0

        size = len(points)
        pq = []
        uf = UnionFind(size)

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                pq.append(edge)

        # convert pq into a heap
        heapq.heapify(pq)

        result = 0
        count = size - 1
        while pq and count > 0:
            edge = heapq.heappop(pq)
            if not uf.is_connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                result += edge.cost
                count -= 1
        return result


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        return f"<Edge ({self.point1}, {self.point2}) ({self.cost})>"


class Solution2:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        size = len(points)
        pq = []

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                pq.append(Edge(i, j, cost))

        heapq.heapify(pq)
        visited = set([0])
        not_visited = set(range(1, size))
        count = size - 1

        cost = 0
        while pq and count > 0:
            to_continue = False
            remain = []

            while not to_continue:
                edge = heapq.heappop(pq)
                if edge.point1 in visited:
                    if edge.point2 in visited:
                        continue
                    if edge.point2 in not_visited:
                        visited.add(edge.point2)
                        not_visited.remove(edge.point2)
                        cost += edge.cost
                        count -= 1
                        to_continue = True
                elif edge.point2 in visited and edge.point1 in not_visited:
                    if edge.point1 in visited:
                        continue
                    if edge.point1 in not_visited:
                        visited.add(edge.point1)
                        not_visited.remove(edge.point1)
                        cost += edge.cost
                        count -= 1
                        to_continue = True
                else:
                    remain.append(edge)

            for edge in remain:
                heapq.heappush(pq, edge)

        return cost


class SolutionPrim:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0

        size = len(points)
        pq = []
        visited = [False] * size
        total = 0
        count = size - 1

        x1, y1 = points[0]
        for j in range(1, size):
            x2, y2 = points[j]
            cost = abs(x1 - x2) + abs(y1 - y2)
            pq.append(Edge(0, j, cost))

        heapq.heapify(pq)

        visited[0] = True
        while pq and count > 0:
            edge = heapq.heappop(pq)
            point2 = edge.point2
            if not visited[point2]:
                total += edge.cost
                visited[point2] = True
                for j in range(size):
                    if not visited[j]:
                        distance = abs(points[point2][0] - points[j][0]) + abs(points[point2][1] - points[j][1])
                        heapq.heappush(pq, Edge(point2, j, distance))
                count -= 1

        return total


def check_cases(s: Solution):
    assert s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18


def test_solution():
    check_cases(Solution())


def test_solution_kruskal():
    check_cases(SolutionKruskal())


def test_solution2():
    check_cases(Solution2())


def test_solution_prim():
    check_cases(SolutionPrim())