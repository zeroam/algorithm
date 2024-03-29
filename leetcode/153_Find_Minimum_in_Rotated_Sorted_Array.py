from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return nums[i + 1]
        return nums[0]


class SolutionBinarySearch:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:  # case 1, 2
            return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[0]:  # case 4
                right = mid - 1
            elif nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return nums[(left + 1) % len(nums)]


class SolutionBinarySearch2:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:  # case 1, 2
            return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1


class SolutionBinarySearch3:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]


def check_cases(s: Solution):
    assert s.findMin([1]) == 1  # case 1
    assert s.findMin([1, 2, 3]) == 1  # case 2
    assert s.findMin([11, 13, 15, 17]) == 11  # case 2
    assert s.findMin([3, 4, 5, 1, 2]) == 1  # case 3
    assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0  # case 3
    assert s.findMin([3, 1, 2]) == 1  # case 4
    assert s.findMin([5, 6, 7, 0, 1, 2, 4]) == 0  # case 4


def test_solution():
    check_cases(Solution())


def test_solution_binary_search():
    check_cases(SolutionBinarySearch())


def test_solution_binary_search2():
    check_cases(SolutionBinarySearch2())


def test_solution_binary_search3():
    check_cases(SolutionBinarySearch3())