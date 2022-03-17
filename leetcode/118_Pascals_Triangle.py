from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if j in [0, i]:
                    row.append(1)
                else:
                    row.append(result[i - 1][j - 1] + result[i - 1][j])
            result.append(row)

        return result


def check_cases(s: Solution):
    assert s.generate(1) == [[1]]
    assert s.generate(2) == [[1], [1, 1]]
    assert s.generate(3) == [[1], [1, 1], [1, 2, 1]]
    assert s.generate(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    assert s.generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]


def test_solution():
    check_cases(Solution())
