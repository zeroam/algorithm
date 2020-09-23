from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        non_obstacles = 0
        start_row, start_col = 0, 0
        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]
                if cell >= 0:
                    non_obstacles += 1
                if cell == 1:
                    start_row = row
                    start_col = col
        
        path_count = 0
        def backtrack(row: int, col: int, remain: int):
            if grid[row][col] == 2 and remain == 1:
                nonlocal path_count
                path_count += 1
                return
            
            temp = grid[row][col]
            grid[row][col] = -4
            remain -= 1
            
            for dir_row, dir_col in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                next_row = row + dir_row
                next_col = col + dir_col

                if not (0 <= next_row < rows and 0 <= next_col < cols):
                    continue
                if grid[next_row][next_col] < 0:
                    continue
                        
                backtrack(next_row, next_col, remain)
                
            grid[row][col] = temp
                
                
        backtrack(start_row, start_col, non_obstacles)

        return path_count


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
