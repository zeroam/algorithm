from abc import ABC, abstractmethod
from collections import deque
from functools import lru_cache
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


class SolutionBacktracking:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []

        def backtrack(cur_node, path):
            if cur_node == target:
                results.append(list(path))
                return

            for next_node in graph[cur_node]:
                path.append(next_node)
                backtrack(next_node, path)
                path.pop()

        backtrack(0, deque([0]))
        return results


class SolutionDP:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        memo = {}
        target = len(graph) - 1

        def all_paths_to_target(cur_node):
            if cur_node in memo:
                return memo[cur_node]

            if cur_node == target:
                return [[target]]

            results = []
            for next_node in graph[cur_node]:
                for path in all_paths_to_target(next_node):
                    results.append([cur_node] + path)

            memo[cur_node] = results
            return results

        return all_paths_to_target(0)


class SolutionDP2:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1

        @lru_cache(maxsize=None)
        def all_paths_to_target(cur_node):
            if cur_node == target:
                return [[target]]

            results = []
            for next_node in graph[cur_node]:
                for path in all_paths_to_target(next_node):
                    results.append([cur_node] + path)

            return results

        return all_paths_to_target(0)


class SolutionBFS:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start, end = 0, len(graph) - 1
        queue = deque([[start]])

        ans = []
        while queue:
            path = queue.popleft()
            cur_node = path[-1]
            if cur_node == end:
                ans.append(path)
                continue

            for next_node in graph[cur_node]:
                queue.append(path + [next_node])

        return ans


def check_cases(s: SolutionBase):
    s.allPathsSourceTarget([[1, 2], [3], [3], []]) == [[0, 1, 3], [0, 2, 3]]
    s.allPathsSourceTarget([[4, 3, 1], [3, 2, 4], [3], [4], []]) == [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]
    s.allPathsSourceTarget([[1], []]) == [[0, 1]]
    s.allPathsSourceTarget([[1, 2, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 2, 3], [0, 3]]
    s.allPathsSourceTarget([[1, 3], [2], [3], []]) == [[0, 1, 2, 3], [0, 3]]
    s.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


def test_solution():
    check_cases(Solution())


def test_solution_backtracking():
    check_cases(SolutionBacktracking())


def test_solution_dp():
    check_cases(SolutionDP())


def test_solution_dp2():
    check_cases(SolutionDP2())


def test_solution_bfs():
    check_cases(SolutionBFS())