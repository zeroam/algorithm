from typing import List
from collections import deque


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        queue = deque([(sr, sc)])
        visited = set([(sr, sc)])
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for r_dir, c_dir in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                    new_r = r + r_dir
                    new_c = c + c_dir
                    if new_r < 0 or new_r >= m or new_c < 0 or new_c >= n:
                        continue

                    if (new_r, new_c) in visited:
                        continue
                    visited.add((new_r, new_c))

                    if image[r][c] == image[new_r][new_c]:
                        queue.append((new_r, new_c))

                image[r][c] = newColor

        return image


class SolutionDFS:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor:
            return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < m:
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < n:
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image


def check_solutions(image: List[List[int]], sr: int, sc: int, new_color: int, expect: List[List[int]]):
    s = Solution()
    s_dfs = SolutionDFS()

    assert s.floodFill(image, sr, sc, new_color) == expect
    assert s_dfs.floodFill(image, sr, sc, new_color) == expect


if __name__ == "__main__":
    check_solutions([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
    check_solutions([[0, 0, 0], [0, 0, 0]], 0, 0, 2, [[2, 2, 2], [2, 2, 2]])
    check_solutions([[0, 0, 0], [0, 1, 1]], 1, 1, 1, [[0, 0, 0], [0, 1, 1]])
