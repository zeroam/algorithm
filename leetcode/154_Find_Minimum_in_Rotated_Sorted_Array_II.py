from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]


class SolutionBinarySearch:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1
        return nums[left]


def check_cases(s: Solution):
    assert s.findMin([1, 3, 5]) == 1
    assert s.findMin([1, 3, 3]) == 1
    assert s.findMin([3, 3, 1, 3]) == 1
    assert s.findMin([2, 2, 2, 0, 1]) == 0
    assert s.findMin([2, 3, 3, 4, 5, 5, 1, 2, 2]) == 1


def test_solution():
    check_cases(Solution())


def test_solution_binary_search():
    check_cases(SolutionBinarySearch())
