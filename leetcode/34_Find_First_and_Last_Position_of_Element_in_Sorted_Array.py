from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            if nums[i] == target:
                result.append(i)

            if nums[i] > target:
                break

        if not result:
            return [-1, -1]
        return min(result), max(result)


def check_cases(s: Solution):
    s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    s.searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    s.searchRange([], 0) == [-1, -1]


def test_solution():
    check_cases(Solution())
