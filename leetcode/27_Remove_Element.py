from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        def remove_element(index, length):
            for i in range(index, length - 1):
                nums[i] = nums[i + 1]

        index = 0
        length = len(nums)
        while index < length:
            if nums[index] == val:
                remove_element(index, length)
                length -= 1
            else:
                index += 1

        return length


class SolutionTwoPointers:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1

        return i


class SolutionTwoPointers2:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


def check_solution(s: Solution, nums: List[int], val: int, expect: List[int]):
    nums_copy = nums.copy()
    size = s.removeElement(nums_copy, val)
    assert nums_copy[:size] == expect


def check_cases(s: Solution):
    check_solution(s, [1, 2, 2, 3, 4], 2, [1, 3, 4])
    check_solution(s, [1, 2, 3, 4], 2, [1, 3, 4])
    check_solution(s, [3, 4, 3, 1], 3, [4, 1])


def test_solution():
    check_cases(Solution())


def test_solution_two_pointers():
    check_cases(SolutionTwoPointers())


def test_solution_two_pointers2():
    check_cases(SolutionTwoPointers2())
