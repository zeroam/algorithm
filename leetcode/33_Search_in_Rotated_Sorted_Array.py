from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        rotated = 0
        while nums[-1] < nums[0]:
            nums.insert(0, nums.pop())
            rotated += 1


        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return (mid + len(nums) - rotated) % len(nums)

        return -1


class SolutionRotatedIndex:
    def search(self, nums: List[int], target: int) -> int:
        def find_rotated_index(left, right):
            if nums[left] < nums[right]:
                return 0

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1

                if nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        def binary_search(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        left, right = 0, n - 1
        rotated_index = find_rotated_index(left, right)

        if nums[rotated_index] == target:
            return rotated_index
        if rotated_index == 0:
            return binary_search(0, len(nums) - 1)

        if nums[0] > target:
            return binary_search(rotated_index, len(nums) - 1)
        return binary_search(0, rotated_index - 1)


def check_cases(s: Solution):
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1


def test_solutino():
    check_cases(Solution())


def test_solution_rotated_index():
    check_cases(SolutionRotatedIndex())
