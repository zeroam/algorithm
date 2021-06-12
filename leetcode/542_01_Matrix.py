from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def nearest_zero(y, x):
            if mat[y][x] == 0:
                return 0

            q = deque([(y, x, 0)])
            visited = {(y, x)}
            while q:
                cur_y, cur_x, dist = q.popleft()
                if mat[cur_y][cur_x] == 0:
                    return dist

                for dir_y, dir_x in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                    new_y, new_x = cur_y + dir_y, cur_x + dir_x
                    if (new_y, new_x) in visited:
                        continue
                    if (
                        new_y < 0
                        or new_y >= len(mat)
                        or new_x < 0
                        or new_x >= len(mat[0])
                    ):
                        continue

                    q.append((new_y, new_x, dist + 1))
                    visited.add((new_y, new_x))

        m, n = len(mat), len(mat[0])
        output = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                output[i][j] = nearest_zero(i, j)

        return output


class SolutionDP:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ans = [[m + n] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    if i > 0:
                        ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1)
                    if j > 0:
                        ans[i][j] = min(ans[i][j], ans[i][j - 1] + 1)

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                else:
                    if i < m - 1:
                        ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1)
                    if j < n - 1:
                        ans[i][j] = min(ans[i][j], ans[i][j + 1] + 1)

        return ans


def check_solutions(mat: List[List[int]], expect: List[List[int]]):
    s = Solution()
    s_dp = SolutionDP()

    assert s.updateMatrix(mat) == expect
    assert s_dp.updateMatrix(mat) == expect


if __name__ == "__main__":
    check_solutions(
        [[0, 0, 0], [0, 1, 0], [0, 0, 0]], [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    )
    check_solutions(
        [[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
    )
    check_solutions(
        [[1, 1, 1, 0], [1, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0]],
        [[3, 2, 1, 0], [2, 1, 0, 0], [1, 1, 0, 1], [0, 0, 1, 0]],
    )
