from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        tmp_count = 0
        for num in nums:
            if num == 1:
                tmp_count += 1
            else:
                max_count = max(max_count, tmp_count)
                tmp_count = 0

        return max(max_count, tmp_count)


def check_solution(array: List[int], expect: int) -> None:
    s = Solution()

    assert s.findMaxConsecutiveOnes(array) == expect


if __name__ == "__main__":
    check_solution([0], 0)
    check_solution([1], 1)
    check_solution([1, 1, 0, 1], 2)
    check_solution([1, 1, 0, 1, 1], 2)
    check_solution([1, 1, 0, 0, 1, 1, 1], 3)
