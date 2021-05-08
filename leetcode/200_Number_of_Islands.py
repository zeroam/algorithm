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


class UnionFind:
    def __init__(self, grid: List[List[str]]):
        m = len(grid)
        n = len(grid[0])

        self.count = 0
        self.parent = [-1] * (m * n)
        self.rank = [-1] * (m * n)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.parent[i * n + j] = i * n + j
                    self.count += 1
                self.rank[i * n + j] = 0

    def find(self, idx: int) -> int:
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

    def union(self, a: int, b: int) -> None:
        rootx = self.find(a)
        rooty = self.find(b)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rooty] > self.rank[rootx]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1


class SolutionDisjointUnion:
    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind(grid)
        # print(f"parent: {uf.parent}, rank: {uf.rank}")

        m = len(grid)
        n = len(grid[0])
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    grid[y][x] = "0"
                    for dir_y, dir_x in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        new_x = x + dir_x
                        new_y = y + dir_y
                        if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:
                            continue
                        if grid[new_y][new_x] == "1":
                            uf.union(y * n + x, new_y * n + new_x)
                            # print(f"parent: {uf.parent}, rank: {uf.rank}")

        return uf.count


def check_solutions(grid: List[List[int]], expect: int):
    s = Solution()
    s_dfs = SolutionDFS()
    s_du = SolutionDisjointUnion()

    assert s.numIslands([row.copy() for row in grid]) == expect
    assert s_dfs.numIslands([row.copy() for row in grid]) == expect
    assert s_du.numIslands([row.copy() for row in grid]) == expect
    print()


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
