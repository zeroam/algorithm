from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                result[i] *= nums[j]
        return result


class SolutionTwoWay:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []

        # left muliple
        p = 1
        for num in nums:
            out.append(p)
            p *= num

        # right multiple
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= p
            p *= nums[i]

        return out


def check_cases(s: Solution):
    assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.productExceptSelf([-1, 1, 0, 3, -3]) == [0, 0, 9, 0, 0]
    assert s.productExceptSelf([0, 0]) == [0, 0]
    assert s.productExceptSelf([0, 4, 0]) == [0, 0, 0]


def test_solution():
    check_cases(Solution())  # Time Limit Exceeded


def test_solution_two_way():
    check_cases(SolutionTwoWay())
