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


def check_cases(s: Solution):
    assert s.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18


def test_solution():
    check_cases(Solution())


def test_solution_kruskal():
    check_cases(SolutionKruskal())
