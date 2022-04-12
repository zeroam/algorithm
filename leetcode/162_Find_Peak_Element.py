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


class SolutionLinear:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1


class SolutionRecursive:
    def findPeakElement(self, nums: List[int]) -> int:
        return self.binary_search(0, len(nums) - 1, nums)

    def binary_search(self, left, right, nums):
        if left == right:
            return left

        mid = (left + right) // 2
        if nums[mid] > nums[mid + 1]:
            return self.binary_search(left, mid, nums)
        return self.binary_search(mid + 1, right, nums)


class SolutionIterative:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


def check_cases(s: Solution):
    assert s.findPeakElement([1]) == 0
    assert s.findPeakElement([1, 2]) == 1
    assert s.findPeakElement([1, 2, 3, 1]) == 2
    assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
    assert s.findPeakElement([3, 1, 2]) in [0, 2]
    assert s.findPeakElement([6, 5, 4, 3, 2, 3 ,2]) == 0


def test_solution():
    check_cases(Solution())


def test_solution_linear():
    check_cases(SolutionLinear())


def test_solution_recursive():
    check_cases(SolutionRecursive())


def test_solution_iterative():
    check_cases(SolutionIterative())
