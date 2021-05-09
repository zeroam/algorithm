import collections
from typing import List


class DSU:
    def __init__(self):
        self.parent = list(range(1001))
        self.rank = [0] * 1001

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[rb] > self.rank[ra]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()
        for edge in edges:
            if not dsu.union(*edge):
                return edge


class SolutionDFS:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and dfs(u, v):
                return [u, v]
            graph[u].add(v)
            graph[v].add(u)


def check_solution(edges: List[List[int]], expect: List[int]) -> None:
    s = Solution()
    s_dfs = SolutionDFS()

    assert s.findRedundantConnection(edges) == expect
    assert s_dfs.findRedundantConnection(edges) == expect


if __name__ == "__main__":
    check_solution([[1, 2], [1, 3], [2, 3]], [2, 3])
    check_solution([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4])
    check_solution([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]], [2, 5])