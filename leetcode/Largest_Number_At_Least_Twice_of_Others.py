from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        index_nums = sorted((num, i) for i, num in enumerate(nums))
        if index_nums[-1][0] >= index_nums[-2][0] * 2:
            return index_nums[-1][1]
        return -1


class Solution2:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        max_value = 0
        pre_max_value = 0
        result = -1
        for i, num in enumerate(nums):
            if num > max_value:
                pre_max_value = max_value
                max_value = num
                result = i
            elif num > pre_max_value:
                pre_max_value = num

        return result if max_value >= pre_max_value * 2 else -1


def check_cases(s: Solution):
    assert s.dominantIndex([3, 6, 1, 0]) == 1
    assert s.dominantIndex([1, 2, 3, 4]) == -1
    assert s.dominantIndex([1]) == 0


def test_solution():
    check_cases(Solution())


def test_solution2():
    check_cases(Solution2())
