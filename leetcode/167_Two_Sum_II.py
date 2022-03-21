from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def search(target: int, start: int, end: int) -> int:
            while start <= end:
                mid = (start + end) // 2
                if numbers[mid] < target:
                    start = mid + 1
                elif numbers[mid] > target:
                    end = mid - 1
                else:
                    return mid
            return -1

        # increase index1, find index2 with binary search
        for index1 in range(len(numbers)):
            num1 = numbers[index1]
            index2 = search(target - num1, index1 + 1, len(numbers) - 1)

            if index2 != -1:
                return [index1 + 1, index2 + 1]


def check_cases(s: Solution):
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2, 3, 4], 6) == [1, 3]
    assert s.twoSum([-1, 0], -1) == [1, 2]


def test_solution():
    check_cases(Solution())
