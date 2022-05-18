import bisect
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        distances = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                bisect.insort(distances, abs(nums[i] - nums[j]))

        return distances[k - 1]


class SolutionBinary:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def possible(guess_dist):
            i = count = 0
            j = 1
            while i < len(nums):
                while j < len(nums) and nums[j] - nums[i] <= guess_dist:
                    j += 1
                count += j - i - 1
                i += 1
            return count >= k

        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1

        return low


def check_cases(s: Solution):
    assert s.smallestDistancePair([1, 3, 1], 1) == 0
    assert s.smallestDistancePair([1, 1, 1], 2) == 0
    assert s.smallestDistancePair([1, 6, 1], 3) == 5


def test_solution():
    check_cases(Solution())


def test_solution_binary():
    check_cases(SolutionBinary())
