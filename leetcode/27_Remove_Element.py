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


def check_solution(nums: List[int], val: int, expect: List[int]):
    solutions = [Solution(), SolutionTwoPointers()]

    for s in solutions:
        nums_copy = nums.copy()
        size = s.removeElement(nums_copy, val)
        assert nums_copy[:size] == expect


if __name__ == "__main__":
    check_solution([1, 2, 2, 3, 4], 2, [1, 3, 4])
    check_solution([1, 2, 3, 4], 2, [1, 3, 4])
    check_solution([3, 4, 3, 1], 3, [4, 1])
