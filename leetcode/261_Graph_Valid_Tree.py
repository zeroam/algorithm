from collections import deque
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.rank = [1 for _ in range(n)]
        self.root = [i for i in range(n)]
        self.count = n
        self.is_tree = True

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y

            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1
        else:
            self.is_tree = False


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)
            if not uf.is_tree:
                return False

        return uf.count == 1 and uf.is_tree


class SolutionIterativeDFS:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        parent = {0: -1}
        stack = [0]

        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in parent:
                    return False
                parent[neighbor] = node
                stack.append(neighbor)

        return len(parent) == n


class SolutionIterativeDFS2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        stack = [0]
        seen = {0}

        while stack:
            node = stack.pop()
            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                stack.append(neighbor)

        return len(seen) == n


class SolutionRecursiveDFS:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = set()

        def dfs(node, parent):
            if node in seen:
                return

            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                if neighbor in seen:
                    return False
                result = dfs(neighbor, node)
                if not result:
                    return False
            return True

        return dfs(0, -1) and len(seen) == n


class SolutionRecursiveDFS2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        seen = set()

        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            for neighbor in adj_list[node]:
                dfs(neighbor)

        dfs(0)
        return len(seen) == n


class SolutionBFS:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        parent = {0: -1}
        queue = deque([0])

        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if neighbor == parent[node]:
                    continue
                if neighbor in parent:
                    return False
                parent[neighbor] = node
                queue.append(neighbor)

        return len(parent) == n


class SolutionBFS2:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        queue = deque([0])
        seen = {0}

        while queue:
            node = queue.popleft()
            for neighbor in adj_list[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)

        return len(seen) == n


def check_cases(s: Solution):
    assert s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
    assert s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
    assert s.validTree(5, [[0, 1], [1, 2], [3, 4]]) == False


def test_solution():
    check_cases(Solution())


def test_solution_iterative_dfs():
    check_cases(SolutionIterativeDFS())


def test_solution_iterative_dfs2():
    check_cases(SolutionIterativeDFS2())


def test_solution_recursive_dfs():
    check_cases(SolutionRecursiveDFS())


def test_solution_recursive_dfs2():
    check_cases(SolutionRecursiveDFS2())


def test_solution_bfs():
    check_cases(SolutionBFS())


def test_solution_bfs2():
    check_cases(SolutionBFS2())
