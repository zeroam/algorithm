from collections import defaultdict, deque
from typing import List


class UnionFind:
    def __init__(self, n: int, s: str):
        self.root = [i for i in range(n)]

    def find(self, x: int) -> int:
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.root[root_y] = root_x


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n, s)
        for x, y in pairs:
            uf.union(x, y)

        parent = [uf.find(i) for i in range(n)]
        d = defaultdict(list)
        for i in range(n):
            d[parent[i]].append(s[i])

        for k in d:
            d[k] = deque(sorted(d[k]))

        ans = []
        for i in range(n):
            key = parent[i]
            ans.append(d[key].popleft())

        return "".join(ans)


def check_cases(s: Solution):
    s.smallestStringWithSwaps("dcab", [[0, 3], [1, 2]])
    s.smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]])


def test_solution():
    check_cases(Solution())
