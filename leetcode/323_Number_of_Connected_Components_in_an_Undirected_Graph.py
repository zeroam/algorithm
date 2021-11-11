from typing import List


class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x: int) -> int:
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            for i in range(len(self.root)):
                if self.root[i] == root_y:
                    self.root[i] = root_x


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for x, y in edges:
            uf.union(x, y)

        return len(set(uf.root))


class UnionFind2:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.count = n

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x
            self.count -= 1


class Solution2:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind2(n)

        for x, y in edges:
            uf.union(x, y)

        return uf.count


class SolutionDFS:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(adj_list: list, visited: set, x: int):
            visited.add(x)
            for neighbor in adj_list[x]:
                if neighbor in visited:
                    continue
                dfs(adj_list, visited, neighbor)

        # make adjlist
        adj_list = [[] for _ in range(n)]
        for x, y in edges:
            adj_list[x].append(y)
            adj_list[y].append(x)

        # iterate and dfs
        visited = set()
        components = 0

        for i in range(n):
            if i in visited:
                continue

            components += 1
            dfs(adj_list, visited, i)

        return components


def check_cases(s: Solution):
    assert s.countComponents(4, [[0, 1], [2, 3], [1, 2]]) == 1
    assert s.countComponents(5, [[0, 1], [1, 2], [3, 4]]) == 2
    assert s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]) == 1


def test_solution():
    check_cases(Solution())


def test_solution2():
    check_cases(Solution2())


def test_solution_dfs():
    check_cases(SolutionDFS())
