from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))


def check_cases(s: Solution):
    s.arrayPairSum([1, 4, 2, 3]) == 4
    s.arrayPairSum([6, 2, 6, 5, 1 ,2]) == 9


def test_solution():
    check_cases(Solution())
