from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def traverse(x: int, y: int) -> int:
            grid[y][x] = "0"  # visited

            queue = [(x, y)]
            while queue:
                x, y = queue.pop(0)

                for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_x = x + dir_x
                    new_y = y + dir_y
                    if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                        continue

                    if grid[new_y][new_x] == "1":
                        queue.append((new_x, new_y))
                        grid[new_y][new_x] = "0"  # visited

            return 1

        ret = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    ret += traverse(x, y)

        return ret


class SolutionDFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(x: int, y: int) -> int:
            grid[y][x] = "0"  # visited

            for dir_x, dir_y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_x = x + dir_x
                new_y = y + dir_y
                if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                    continue

                if grid[new_y][new_x] == "1":
                    dfs(new_x, new_y)

        ret = 0
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    dfs(x, y)
                    ret += 1

        return ret


def check_solutions(grid: List[List[int]], expect: int):
    s = Solution()
    s_dfs = SolutionDFS()

    assert s.numIslands([row.copy() for row in grid]) == expect
    assert s_dfs.numIslands([row.copy() for row in grid]) == expect


if __name__ == "__main__":
    check_solutions(
        [
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "0", "1", "1", "0"],
            ["0", "0", "1", "1", "0"],
            ["1", "1", "0", "0", "1"],
            ["1", "1", "0", "0", "1"],
        ],
        5,
    )

    check_solutions(
        [
            ["1", "1", "1", "1", "1"],
            ["1", "1", "0", "0", "1"],
            ["0", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "0", "0", "1"],
        ],
        1,
    )
