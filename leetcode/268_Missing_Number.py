from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        all_nums = set(range(len(nums) + 1))

        for num in nums:
            all_nums.remove(num)

        return list(all_nums)[0]


class SolutionDiff:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums) + 1)) - sum(nums)


class SolutionMath:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n + 1) * n // 2
        return total - sum(nums)


def test_solution():
    s = Solution()
    check_solutions(s)


def test_solution_diff():
    s = SolutionDiff()
    check_solutions(s)


def test_solution_math():
    s = SolutionDiff()
    check_solutions(s)


def check_solutions(s: Solution):
    assert s.missingNumber([0]) == 1
    assert s.missingNumber([1, 2]) == 0
    assert s.missingNumber([0, 2]) == 1
    assert s.missingNumber([0, 1]) == 2
    assert s.missingNumber([3, 1, 0]) == 2
    assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
