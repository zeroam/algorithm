from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]


def check_cases(s: Solution):
    s.findDuplicate([1, 3, 4, 2, 2]) == 2
    s.findDuplicate([3, 1, 3, 4, 2]) == 3
    s.findDuplicate([1, 4, 4, 2, 4]) == 4


def test_solution():
    check_cases(Solution())
