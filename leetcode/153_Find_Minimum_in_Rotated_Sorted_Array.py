from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]


def check_cases(s: Solution):
    assert s.findMin([3, 4, 5, 1, 2]) == 1
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert s.findMin([5, 6, 7, 0, 1, 2, 4]) == 0
    assert s.findMin([11, 13, 15, 17]) == 11
    assert s.findMin([3, 1, 2]) == 1


def test_solution():
    check_cases(Solution())
