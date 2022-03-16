from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        index = 0

        x, y = 0, 0
        visited = {(x, y), (0, n), (m, n - 1), (m - 1, -1)}
        result = [matrix[x][y]]
        while len(visited) < m * n + 3:
            index = index % len(directions)
            x_dir, y_dir = directions[index]

            next_x, next_y = x + x_dir, y + y_dir
            if (next_x, next_y) in visited:
                index += 1
                continue

            x, y = next_x, next_y
            result.append(matrix[x][y])
            visited.add((x, y))

        return result



def check_cases(s: Solution):
    assert s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_solution():
    check_cases(Solution())
