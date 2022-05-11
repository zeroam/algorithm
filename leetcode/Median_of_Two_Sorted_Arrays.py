from tkinter import W
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge
        pt1, pt2 = 0, 0
        nums = []
        while pt1 < len(nums1):
            if pt2 == len(nums2) or nums1[pt1] <= nums2[pt2]:
                nums.append(nums1[pt1])
                pt1 += 1
            else:
                nums.append(nums2[pt2])
                pt2 += 1
        while pt2 < len(nums2):
            nums.append(nums2[pt2])
            pt2 += 1

        # find median
        size = len(nums)
        if size % 2 == 1:
            return nums[size // 2]
        return (nums[size // 2 - 1] + nums[size // 2]) / 2


def check_cases(s: Solution):
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([1, 3], [2, 4]) == 2.5


def test_solution():
    check_cases(Solution())
