from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1


class SolutionLeftSum:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            if left_sum == total - left_sum - num:
                return i
            left_sum += num

        return -1


def check_cases(s: Solution):
    assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert s.pivotIndex([1, 2, 3]) == -1
    assert s.pivotIndex([2, 1, -1]) == 0
    assert s.pivotIndex([-1, -1, -1, -1, 0, 1]) == 1


def test_solution():
    check_cases(Solution())


def test_solution_left_sum():
    check_cases(SolutionLeftSum())
