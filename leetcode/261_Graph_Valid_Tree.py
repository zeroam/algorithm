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


def check_cases(s: Solution):
    assert s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]) == True
    assert s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]) == False
    assert s.validTree(5, [[0, 1], [1, 2], [3, 4]]) == False


def test_solution():
    check_cases(Solution())
