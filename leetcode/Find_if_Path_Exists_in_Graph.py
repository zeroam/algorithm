from abc import ABC, abstractmethod
from collections import defaultdict
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


def check_cases(s: SolutionInterface):
    assert s.validPath(1, [], 0, 0) == True
    assert s.validPath(3, [[0, 1], [1, 2], [2, 0], [0, 2]], 0, 2) == True
    assert s.validPath(6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5) == False



def test_solution():
    check_cases(Solution())
