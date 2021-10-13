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
