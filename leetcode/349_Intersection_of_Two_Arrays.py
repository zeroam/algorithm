from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)

        return nums1_set & nums2_set


def test_solution():
    s = Solution()

    assert s.intersection([1, 2, 2, 1], [2, 2]) == set([2])
    assert s.intersection([4, 9, 5], [4, 9]) == set([4, 9])
