from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n = 0
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        
        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                if value == 1:
                    start_y = i
                    start_x = j
                    visited[i][j] = 1
                elif value in [0, 2]:
                    n += 1
                else:
                    visited[i][j] = 1
        
        paths = [(start_y), (start_x)]
        result = 0
        def dfs(x: int, y: int, walk_cnt: int = 0):
            if walk_cnt >= n:
                if grid[y][x] == 2:
                    nonlocal result
                    result += 1
                return
            
            row = len(grid)
            col = len(grid[0])
            
            for dir_x, dir_y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_x = x + dir_x
                next_y = y + dir_y

                if 0 <= next_x < col and 0 <= next_y < row:
                    if visited[next_y][next_x] != 0:
                        continue
                        
                    visited[next_y][next_x] = 1
                    paths.append((next_y, next_x))
                    dfs(next_x, next_y, walk_cnt + 1)
                    visited[next_y][next_x] = 0
                    paths.pop()
                
        dfs(start_x, start_y)

        return result


if __name__ == "__main__":
    s = Solution()

    grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
    expect = 2
    assert s.uniquePathsIII(grid) == expect

    grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
    expect= 4
    assert s.uniquePathsIII(grid) == expect

    grid = [[0, 1], [2, 0]]
    expect = 0
    assert s.uniquePathsIII(grid) == expect
