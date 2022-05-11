import bisect
from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        distances = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                bisect.insort(distances, abs(nums[i] - nums[j]))

        return distances[k - 1]


def check_cases(s: Solution):
    assert s.smallestDistancePair([1, 3, 1], 1) == 0
    assert s.smallestDistancePair([1, 1, 1], 2) == 0
    assert s.smallestDistancePair([1, 6, 1], 3) == 5


def test_solution():
    check_cases(Solution())
