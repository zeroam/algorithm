from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        BOX_SIZE = 3
        BOARD_SIZE = 9

        def _row_invalid(row_index: int, col_index: int, num: int) -> bool:
            if num == ".":
                return False

            for i in range(BOARD_SIZE):
                if num == board[row_index][i] and i != col_index:
                    return True
            return False

        def _col_invalid(row_index: int, col_index: int, num: int) -> bool:
            if num == ".":
                return False

            for i in range(BOARD_SIZE):
                if num == board[i][col_index] and i != row_index:
                    return True
            return False

        def _box_invalid(row_index: int, col_index: int, num: int) -> bool:
            if num == ".":
                return False

            row_start = row_index - row_index % BOX_SIZE
            col_start = col_index - col_index % BOX_SIZE

            for i in range(row_start, row_start + BOX_SIZE):
                for j in range(col_start, col_start + BOX_SIZE):
                    if num == board[i][j] and i != row_index and j != col_index:
                        return True
            return False

        for i, row in enumerate(board):
            for j, num in enumerate(row):
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


def test_solution():
    check_cases(Solution())
