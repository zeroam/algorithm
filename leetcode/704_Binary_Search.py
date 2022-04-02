from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid

        return -1


def check_cases(s: Solution):
    s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    s.search([-1, 0, 3, 5, 9, 12], 2) == -1


def test_solution():
    check_cases(Solution())
