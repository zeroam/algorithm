import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        origin_total = 0
        for size in range(1, len(nums) + 1):
            origin_total = total = origin_total + nums[size - 1]
            if total >= target:
                return size

            for i in range(0, len(nums) - size):
                total = total - nums[i] + nums[i + size]
                if total >= target:
                    return size

        return 0


class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * n
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]

        for size in range(0, n):
            for i in range(size, n):
                total = sums[i] - sums[i - size] + nums[i - size]
                if total >= target:
                    return size + 1
        return 0


class SolutionBruteForce:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        sums = [0] * n
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]

        ans = sys.maxsize
        for i in range(n):
            for j in range(i, n):
                total = sums[j] - sums[i] + nums[i]
                if total >= target:
                    ans = min(ans, j - i + 1)
                    break
        return ans if ans != sys.maxsize else 0


class SolutionTwoPointers:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        ans = sys.maxsize
        left = 0
        total = 0
        for i in range(n):
            total += nums[i]
            while total >= target:
                ans = min(ans, i - left + 1)
                total -= nums[left]
                left += 1
        return ans if ans != sys.maxsize else 0


def check_cases(s: Solution):
    assert s.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
    assert s.minSubArrayLen(213, [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]) == 8
    assert s.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
    assert s.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5


def test_solution():
    check_cases(Solution())


def test_solution2():
    check_cases(Solution2())


def test_solution_brute_force():
    check_cases(SolutionBruteForce())


def test_solution_two_pointers():
    check_cases(SolutionTwoPointers())
