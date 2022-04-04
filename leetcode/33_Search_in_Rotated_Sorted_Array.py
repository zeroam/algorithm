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


def check_cases(s: Solution):
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([1], 0) == -1


def test_solutino():
    check_cases(Solution())
