from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1] * (i + 1) for i in range(rowIndex + 1)]
        if rowIndex < 2:
            return rows[-1]

        for i in range(2, rowIndex + 1):
            pre_row = rows[i - 1]
            row = rows[i]

            for j in range(1, i):
                row[j] = pre_row[j - 1] + pre_row[j]

        return rows[-1]


def check_cases(s: Solution):
    assert s.getRow(3) == [1, 3, 3, 1]
    assert s.getRow(0) == [1]
    assert s.getRow(1) == [1, 1]


def test_solution():
    check_cases(Solution())
