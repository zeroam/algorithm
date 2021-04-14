from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        rise = False
        down = False

        for i in range(len(arr) - 1):
            if arr[i] == arr[i + 1]:
                return False

            if not rise:
                if arr[i] < arr[i + 1]:
                    rise = True
                else:
                    return False
            elif rise and down and arr[i] < arr[i + 1]:
                return False
            elif rise and arr[i] > arr[i + 1]:
                down = True

        return rise and down


class SolutionOneWay:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        i = 0

        # walk up
        while i + 1 < length and arr[i] < arr[i + 1]:
            i += 1


        if i == 0 or i == length - 1:
            return False

        # walk down
        while i + 1 < length and arr[i] > arr[i + 1]:
            i += 1

        return i == length - 1


def check_solutions(arr: List[int], expect: bool):
    s = Solution()
    s_ow = SolutionOneWay()

    assert s.validMountainArray(arr) == expect
    assert s_ow.validMountainArray(arr) == expect


if __name__ == "__main__":
    check_solutions([2, 1], False)
    check_solutions([3, 5, 5], False)
    check_solutions([0, 3, 2, 1], True)
    check_solutions([3, 4, 5, 5, 3, 1], False)
