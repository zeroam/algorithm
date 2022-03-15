from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def next_start(x: int, y: int):
            if y == len(mat[0]) - 1:
                x += 1
            else:
                y += 1
            return x, y

        def traverse(x: int, y: int) -> List[int]:
            result = []
            while x < len(mat) and y >= 0:
                result.append(mat[x][y])
                x += 1
                y -= 1

            return result if (x + y) % 2 == 1 else result[::-1]

        x, y = 0, 0
        result = []
        while x < len(mat) and y < len(mat[0]):
            result += traverse(x, y)
            x, y = next_start(x, y)

        return result


def check_cases(s: Solution):
    assert s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert s.findDiagonalOrder([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_solution():
    check_cases(Solution())
