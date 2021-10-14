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