from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            if nums[i] == target:
                result.append(i)

            if nums[i] > target:
                break

        if not result:
            return [-1, -1]
        return min(result), max(result)


class SolutionBinarySearch:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lower_bound = self.find_bound(nums, target, True)
        if lower_bound == -1:
            return [-1, -1]

        upper_bound = self.find_bound(nums, target, False)

        return [lower_bound, upper_bound]

    def find_bound(self, nums, target, is_first):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if is_first:
                    if mid == left or nums[mid - 1] < target:
                        return mid
                    right = mid - 1
                else:
                    if mid == right or nums[mid + 1] > target:
                        return mid
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1


def check_cases(s: Solution):
    s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    s.searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
    s.searchRange([], 0) == [-1, -1]


def test_solution():
    check_cases(Solution())


def test_solution_binary_search():
    check_cases(SolutionBinarySearch())
