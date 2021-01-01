from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        used = [0] * len(arr)

        for piece in pieces:
            start_index = self._find_index(arr, piece[0])
            if start_index == -1:
                return False

            for i, num in enumerate(piece):
                if start_index + i >= n:
                    return False
                if num != arr[start_index + i]:
                    return False

                used[start_index + i] += 1

        for cnt in used:
            if cnt != 1:
                return False

        return True


    def _find_index(self, l: list, n: int):
        for i, num in enumerate(l):
            if n == num:
                return i
        return -1


def check(arr: list, pieces: list, expect: bool):
    s = Solution()

    assert s.canFormArray(arr, pieces) == expect


if __name__ == "__main__":
    # case 1
    arr = [85]
    pieces = [[85]]
    expect = True
    check(arr, pieces, expect)

    # case 2
    arr = [15, 88]
    pieces = [[88], [15]]
    expect = True
    check(arr, pieces, expect)

    # case 3
    arr = [49, 18, 16]
    pieces = [[16, 18, 49]]
    expect = False
    check(arr, pieces, expect)

    # case 4
    arr = [91, 4, 64, 78]
    pieces = [[78], [4, 64], [91]]
    expect = True
    check(arr, pieces, expect)

    # case 5
    arr = [1, 3, 5, 7]
    pieces = [[2, 4, 6, 8]]
    expect = False
    check(arr, pieces, expect)
