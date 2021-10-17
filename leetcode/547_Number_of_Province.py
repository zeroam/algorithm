from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        root = [i for i in range(n)]

        def union(x, y):
            root_x = root[x]
            root_y = root[y]
            if root_x > root_y:
                root_x, root_y = root_y, root_x
            for i in range(n):
                if root[i] == root_y:
                    root[i] = root_x

        for i in range(n):
            for j in range(i + 1, n):
                connected = isConnected[i][j]
                if connected:
                    union(i, j)

        print(root)
        return len(set(root))


class SolutionDFS:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0 for _ in range(n)]

        def dfs(i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and visited[j] == 0:
                    visited[j] = 1
                    dfs(j)

        count = 0
        for i in range(n):
            if visited[i] == 0:
                dfs(i)
                count += 1

        return count


class SolutionBFS:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0 for _ in range(n)]
        queue = deque()

        count = 0
        for i in range(n):
            if visited[i] == 0:
                queue.append(i)
                while queue:
                    s = queue.popleft()
                    visited[s] = 1
                    for j in range(n):
                        if isConnected[s][j] == 1 and visited[j] == 0:
                            queue.append(j)
                count += 1

        return count


class SolutionUnion:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xset = find(x)
            yset = find(y)
            if xset != yset:
                parent[yset] = xset

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        count = 0
        for i, p in enumerate(parent):
            if p == i:
                count += 1

        return count


class UnionFind:
    def __init__(self, n: int):
        self.root = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.count = n

    def find(self, x: int) -> int:
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x: int, y: int) -> None:
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

    def get_count(self):
        return self.count

class SolutionUnionFind:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.get_count()


def check_cases(s: Solution):
    assert s.findCircleNum(
        [
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1],
        ]
    ) == 1

    assert s.findCircleNum(
        [
            [1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 1],
        ]
    ) == 5

def test_solution():
    check_cases(Solution())


def test_solution_dfs():
    check_cases(SolutionDFS())


def test_solution_bfs():
    check_cases(SolutionBFS())


def test_solution_union():
    check_cases(SolutionUnion())


def test_solution_union_find():
    check_cases(SolutionUnionFind())
