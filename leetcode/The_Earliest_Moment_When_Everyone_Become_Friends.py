from typing import List


class UnionFind:
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


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        uf = UnionFind(n)

        for timestamp, x, y in sorted(logs):
            uf.union(x, y)
            if uf.count == 1:
                return timestamp

        return -1


def check_cases(s: Solution):
    assert s.earliestAcq([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6) == 20190301
    assert s.earliestAcq([[0, 2, 0], [1, 0, 1], [3, 0, 3], [4, 1, 2], [7, 3, 1]], 4) == 3
    assert s.earliestAcq([[7, 3, 1], [4, 1, 2], [3, 0, 3], [1, 0, 1], [0, 2, 0]], 4) == 3


def test_solution():
    check_cases(Solution())
