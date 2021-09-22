from collections import defaultdict
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        sums1 = defaultdict(lambda: 0)
        sums2 = defaultdict(lambda: 0)

        for num1 in nums1:
            for num2 in nums2:
                sums1[num1 + num2] += 1

        for num3 in nums3:
            for num4 in nums4:
                sums2[num3 + num4] += 1

        for num1, cnt1 in sums1.items():
            for num2, cnt2 in sums2.items():
                if num1 + num2 == 0:
                    ans += cnt1 * cnt2

        return ans


class SolutionHashMap:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ans = 0
        sums = defaultdict(lambda: 0)

        for num1 in nums1:
            for num2 in nums2:
                sums[num1 + num2] += 1

        for num3 in nums3:
            for num4 in nums4:
                ans += sums[-(num3 + num4)]

        return ans


def check_cases(s: Solution):
    assert s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
    assert s.fourSumCount([0], [0], [0], [0]) == 1


def test_solution():
    check_cases(Solution())


def test_solution_hash_map():
    check_cases(SolutionHashMap())
