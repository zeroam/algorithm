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


class SolutionRecursive:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        prev_row = self.getRow(rowIndex - 1)
        row = [1] * (rowIndex + 1)
        for i in range(1, len(prev_row)):
            row[i] = prev_row[i - 1] + prev_row[i]

        return row


class SolutionDynamic:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1]
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                result[j] = result[j] + result[j - 1]
            result.append(1)

        return result


def check_cases(s: Solution):
    assert s.getRow(3) == [1, 3, 3, 1]
    assert s.getRow(0) == [1]
    assert s.getRow(1) == [1, 1]


def test_solution():
    check_cases(Solution())


def test_solution_recursive():
    check_cases(SolutionRecursive())


def test_solution_dynamic_programming():
    check_cases(SolutionDynamic())
