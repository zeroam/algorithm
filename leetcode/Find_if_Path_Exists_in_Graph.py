from abc import ABC, abstractmethod
from collections import defaultdict, deque
from typing import List


class SolutionInterface(ABC):
    @abstractmethod
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        ...


class Solution:
    def traverse_graph(self, cur_node, target_node, visited, graph):
        if cur_node == target_node:
            return True

        visited.add(cur_node)
        neighbors = graph[cur_node]
        for next_node in neighbors:
            if next_node in visited:
                continue
            ret = self.traverse_graph(next_node, target_node, visited, graph)
            if ret:
                return True

        return False

    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if start == end:
            return True

        # make graph
        graph = defaultdict(set)
        for node_1, node_2 in edges:
            graph[node_1].add(node_2)
            graph[node_2].add(node_1)

        # traverse
        visited = set([start])
        return self.traverse_graph(start, end, visited, graph)


class SolutionDFS:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # make graph
        graph = defaultdict(set)
        for node_1, node_2 in edges:
            graph[node_1].add(node_2)
            graph[node_2].add(node_1)

        # traverse
        stack = [start]
        visited = set()
        while stack:
            cur_node = stack.pop()
            if cur_node == end:
                return True

            visited.add(cur_node)
            neighbors = graph[cur_node]
            for next_node in neighbors:
                if next_node in visited:
                    continue
                stack.append(next_node)

        return False


class SolutionBFS:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        # make graph
        graph = defaultdict(set)
        for node_1, node_2 in edges:
            graph[node_1].add(node_2)
            graph[node_2].add(node_1)

        # traverse
        queue = deque([start])
        visited = set()
        while queue:
            cur_node = queue.popleft()
            if cur_node == end:
                return True

            visited.add(cur_node)
            neighbors = graph[cur_node]
            for next_node in neighbors:
                if next_node in visited:
                    continue
                queue.append(next_node)

        return False


class UnionFind:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]

    def find(self, x: int):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x

    def is_connected(self, x: int, y: int):
        return self.find(x) == self.find(y)


class SolutionUnionFind:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        uf = UnionFind(n)
        for node_1, node_2 in edges:
            uf.union(node_1, node_2)

        return uf.is_connected(start, end)




def check_cases(s: SolutionInterface):
    assert s.validPath(1, [], 0, 0) == True
    assert s.validPath(3, [[0, 1], [1, 2], [2, 0], [0, 2]], 0, 2) == True
    assert s.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) == False



def test_solution():
    check_cases(Solution())


def test_solution_dfs():
    check_cases(SolutionDFS())


def test_solution_bfs():
    check_cases(SolutionBFS())


def test_solution_union_find():
    check_cases(SolutionUnionFind())
