from abc import ABC, abstractmethod
from typing import List


class SolutionBase(ABC):
    @abstractmethod
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ...


class Solution(SolutionBase):
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []

        def find_path(cur_node, target_node, visited, graph, path):
            visited.add(cur_node)
            path.append(cur_node)
            if cur_node == target_node:
                paths.append(path.copy())

            neighbors = graph[cur_node]
            for next_node in neighbors:
                if next_node in visited:
                    continue
                find_path(next_node, target_node, visited, graph, path)

            visited.remove(cur_node)
            path.remove(cur_node)

        start, end = 0, len(graph) - 1
        find_path(start, end, set(), graph, [])

        return paths


def check_cases(s: SolutionBase):
    s.allPathsSourceTarget([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
    s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    s.allPathsSourceTarget([[1], []]) == [[0, 1]]
    s.allPathsSourceTarget([[1, 2, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 2, 3], [0, 3]]
    s.allPathsSourceTarget([[1, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 3]]


def test_solution():
    check_cases(Solution())
