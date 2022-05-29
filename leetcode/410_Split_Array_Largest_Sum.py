from functools import lru_cache
import itertools
import sys
from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        largest_sum = sys.maxsize

        def make_cases(start: int, case: List[int] = []):
            nonlocal largest_sum
            if len(case) == m - 1:
                case.append(len(nums))
                prev = 0
                max_value = 0
                for cur in case:
                    max_value = max(max_value, sum(nums[prev:cur]))
                    prev = cur

                if max_value < largest_sum:
                    largest_sum = max_value

            for i in range(start, len(nums) + 1):
                temp = case.copy()
                case.append(i)
                make_cases(i + 1, temp)

        make_cases(1)
        return largest_sum


class SolutionDynamic:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        acc_nums = [0] + list(itertools.accumulate(nums))

        @lru_cache(None)
        def split_sums(curr_index: int, arr_cnt: int) -> int:
            if arr_cnt == 1:
                return acc_nums[n] - acc_nums[curr_index]

            min_sum = acc_nums[n]
            for i in range(curr_index, n - arr_cnt + 1):
                first_sum = acc_nums[i + 1] - acc_nums[curr_index]
                largest_sum = max(first_sum, split_sums(i + 1, arr_cnt - 1))
                min_sum = min(min_sum, largest_sum)
                if first_sum >= min_sum:
                    break

            return min_sum

        return split_sums(0, m)


def check_cases(s: Solution):
    s.splitArray([7, 2, 5, 10, 8], 2) == 18
    s.splitArray([1, 2, 3, 4, 5], 2) == 9
    s.splitArray([1, 4, 4], 3) == 4


def test_solution():
    check_cases(Solution())


def test_solution_dynamic():
    check_cases(SolutionDynamic())
