from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))


def check_cases(s: Solution):
    assert s.arrayPairSum([1, 4, 3, 2]) == 4
    assert s.arrayPairSum([6, 2, 6, 5, 1, 2]) == 9
    assert s.arrayPairSum([7, 0, 6, 4, 9, 6]) == 13


def test_solution():
    check_cases(Solution())
