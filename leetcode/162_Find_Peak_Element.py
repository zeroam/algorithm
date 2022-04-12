from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2

            pre_value = nums[mid - 1] if mid > 0 else nums[mid] - 1
            cur_value = nums[mid]
            next_value = nums[mid + 1] if mid < len(nums) else nums[mid] - 1

            if cur_value > pre_value and cur_value > next_value:
                return mid
            elif pre_value < cur_value < next_value:
                left = mid + 1
            else:
                right = mid

        return left


def check_cases(s: Solution):
    assert s.findPeakElement([1]) == 0
    assert s.findPeakElement([1, 2]) == 1
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
    assert s.findPeakElement([3, 1, 2]) == 0


def test_solution():
    check_cases(Solution())
