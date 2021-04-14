from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] * 2 == arr[j] or arr[j] * 2 == arr[i]:
                    return True
        return False


def check_solutions(arr: List[int], expect: bool):
    s = Solution()

    assert s.checkIfExist(arr) == expect


if __name__ == "__main__":
    check_solutions([10, 2, 5, 3], True)
    check_solutions([7, 1, 14, 11], True)
    check_solutions([3, 1, 7, 11], False)
