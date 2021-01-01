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

class SolutionOneByOne:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        i = 0
        while i < n:
            for p in pieces:
                if p[0] == arr[i]:
                    break
            else:
                return False

            for x in p:
                if x != arr[i]:
                    return False

                i += 1

        return True


class SolutionBS:
    def _binary_search(self, arr: List[List[int]], num: int) -> int:
        n = len(arr)

        left = 0
        right = n - 1
        found = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid][0] < num:
                left = mid + 1
            elif arr[mid][0] > num:
                right = mid - 1
            else:
                found = mid
                break

        return found


    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        i = 0
        pieces.sort()

        while i < n:
            found = self._binary_search(pieces, arr[i])
            if found == -1:
                return False

            p = pieces[found]
            for x in p:
                if x != arr[i]:
                    return False

                i += 1

        return True


class SolutionHashMap:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        n = len(arr)
        # initialize hashmap
        mapping = {p[0]: p for p in pieces}

        i = 0
        while i < n:
            if arr[i] not in mapping:
                return False

            p = mapping[arr[i]]
            for x in p:
                if x != arr[i]:
                    return False

                i += 1

        return True


def check(arr: list, pieces: list, expect: bool):
    s = Solution()
    s_o = SolutionOneByOne()
    s_bs = SolutionBS()
    s_hm = SolutionHashMap()

    assert s.canFormArray(arr, pieces) == expect
    assert s_o.canFormArray(arr, pieces) == expect
    assert s_bs.canFormArray(arr, pieces) == expect
    assert s_hm.canFormArray(arr, pieces) == expect


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
