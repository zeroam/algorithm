from typing import List

from common.utils import time_elpased


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOX_SIZE = 3
        BOARD_SIZE = 9

        def _row_invalid(row_index: int, col_index: int, num: int) -> bool:
            for i in range(BOARD_SIZE):
                if num == board[row_index][i] and i != col_index:
                    return True
            return False

        def _col_invalid(row_index: int, col_index: int, num: int) -> bool:
            for i in range(BOARD_SIZE):
                if num == board[i][col_index] and i != row_index:
                    return True
            return False

        def _box_invalid(row_index: int, col_index: int, num: int) -> bool:
            row_start = row_index - row_index % BOX_SIZE
            col_start = col_index - col_index % BOX_SIZE

            for i in range(row_start, row_start + BOX_SIZE):
                for j in range(col_start, col_start + BOX_SIZE):
                    if num == board[i][j] and i != row_index and j != col_index:
                        return True
            return False

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue

                if _row_invalid(i, j, num):
                    print("row invalid", i, j, num)
                    return False

                if _col_invalid(i, j, num):
                    print("col invalid", i, j, num)
                    return False

                if _box_invalid(i, j, num):
                    print("box invalid", i, j, num)
                    return False

        return True


class SolutionHashSet:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = 9

        rows = [set() for _ in range(BOARD_SIZE)]
        cols = [set() for _ in range(BOARD_SIZE)]
        boxes = [set() for _ in range(BOARD_SIZE)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue

                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)

                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

        return True


class SolutionFixedLengthArray:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOARD_SIZE = 9

        rows = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        cols = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        boxes = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]

        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num == ".":
                    continue

                pos = int(num) - 1

                if rows[i][pos] == 1:
                    return False
                rows[i][pos] = 1

                if cols[j][pos] == 1:
                    return False
                cols[j][pos] = 1

                box_index = (i // 3) * 3 + (j // 3)
                if boxes[box_index][pos] == 1:
                    return False
                boxes[box_index][pos] = 1

        return True


def check_cases(s: Solution):
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku(board) == True

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert s.isValidSudoku(board) == False


@time_elpased
def test_solution():
    check_cases(Solution())


@time_elpased
def test_solution_hashset():
    check_cases(SolutionHashSet())


@time_elpased
def test_solution_fixed_length_array():
    check_cases(SolutionFixedLengthArray())
