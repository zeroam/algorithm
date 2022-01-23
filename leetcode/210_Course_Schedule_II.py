from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 1:
            return [0]

        # make adjlist
        adj_list = [set() for _ in range(numCourses)]
        for to_node, pre_node in prerequisites:
            adj_list[to_node].add(pre_node)

        dq = deque()
        visited = [False] * numCourses
        for node, pre_nodes in enumerate(adj_list):
            if len(pre_nodes) == 0:
                dq.append(node)
                visited[node] = True

        # add queue to node which adjlist is empty
        ans = []
        while dq:
            cur_node = dq.popleft()
            print(dq, cur_node, adj_list)
            for node, pre_nodes in enumerate(adj_list):
                if visited[node]:
                    continue

                if cur_node in pre_nodes:
                    pre_nodes.remove(cur_node)
                if len(pre_nodes) == 0:
                    dq.append(node)
                    visited[node] = True

            ans.append(cur_node)

        if len(ans) != numCourses:
            return []
        return ans


class SolutionDFS:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # make adjlist
        adj_list = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        stack = []
        colors = [self.WHITE] * numCourses
        is_cycle = False

        def dfs(node):
            nonlocal is_cycle
            if is_cycle:
                return

            colors[node] = self.GRAY

            for nei in adj_list[node]:
                if colors[nei] == self.WHITE:
                    dfs(nei)
                elif colors[nei] == self.GRAY:
                    is_cycle = True

            colors[node] = self.BLACK
            stack.append(node)

        for node in range(numCourses):
            if colors[node] == self.WHITE:
                dfs(node)

        if is_cycle:
            return []
        return stack[::-1]


class SolutionKahns:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        degrees = [0] * numCourses
        for dest, src in prerequisites:
            graph[src].append(dest)
            degrees[dest] += 1

        # add to queue
        queue = deque([node for node, degree in enumerate(degrees) if degree == 0])

        ans = []
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                degrees[nei] -= 1
                if degrees[nei] == 0:
                    queue.append(nei)

            ans.append(node)

        return ans if len(ans) == numCourses else []



def check_cases(s: Solution):
    assert s.findOrder(2, [[1, 0]]) == [0, 1]
    assert s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) in ( [0, 1, 2, 3], [0, 2, 1, 3])
    assert s.findOrder(1, []) == [0]
    assert s.findOrder(2, [[0, 1], [1, 0]]) == []


def test_solution():
    check_cases(Solution())


def test_solution_dfs():
    check_cases(SolutionDFS())


def test_solution_dfs_kahns():
    check_cases(SolutionKahns())
