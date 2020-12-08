from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret = [[-1] * n for _ in range(n)]
        
        x_dir = False
        y_dir = True
        x = 0
        y = 0
        dir_value = 1
        for i in range(1, n * n + 1):
            ret[x][y] = i
            
            if y_dir:
                y += dir_value
                y_next = y + dir_value
                if y_next < 0 or y_next >= n or ret[x][y_next] != -1:
                    x_dir = True
                    y_dir = False
                
            elif x_dir:
                x += dir_value
                x_next = x + dir_value
                if x_next < 0 or x_next >=  n or ret[x_next][y] != -1:
                    x_dir = False
                    y_dir = True
                    dir_value *= -1
                    
        return ret
        

if __name__ == "__main__":
    s = Solution()

    n = 1
    expect = [[1]]
    assert s.generateMatrix(n) == expect

    n = 2
    expect = [[1, 2], [4, 3]]
    assert s.generateMatrix(n) == expect

    n = 3
    expect = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    assert s.generateMatrix(n) == expect
