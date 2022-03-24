from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            num = nums.pop()
            nums.insert(0, num)


class SolutionBruteForce:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            prev = nums[-1]
            for i, cur in enumerate(nums):
                nums[i] = prev
                prev = cur


class SolutionExtraArray:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        temp = [0] * n
        for i in range(n):
            temp[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = temp[i]


class SolutionCyclicReplacement:
    def rotate(self, nums: List[int], k: int) -> None:
        count = 0
        start, pt = 0, 0
        prev = nums[pt]
        while True:
            pt = (pt + k) % len(nums)
            cur = nums[pt]
            nums[pt] = prev

            count += 1
            if count >= len(nums):
                break

            prev = cur
            if pt == start:
                pt += 1
                start += 1
                prev = nums[pt]


def check_cases(s: Solution):
    nums = [1, 2, 3, 4, 5]
    s.rotate(nums, 3)
    assert nums == [3, 4, 5, 1, 2]

    nums = [1, 2, 3, 4, 5, 6, 7]
    s.rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]

    nums = [-1, -100, 3, 99]
    s.rotate(nums, 2)
    assert nums == [3, 99, -1, -100]

    nums = [1]
    s.rotate(nums, 0)
    assert nums == [1]


def test_solution():
    check_cases(Solution())


def test_solution_brute_force():
    check_cases(SolutionBruteForce())


def test_solution_extra_array():
    check_cases(SolutionExtraArray())


def test_solution_cyclic_replacement():
    check_cases(SolutionCyclicReplacement())
