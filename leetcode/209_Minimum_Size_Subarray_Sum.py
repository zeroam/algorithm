from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for size in range(1, len(nums) + 1):
            total = sum(nums[0:size])
            if total >= target:
                return size

            for i in range(0, len(nums) - size):
                total = total - nums[i] + nums[i + size]
                if total >= target:
                    return size

        return 0




def check_cases(s: Solution):
    assert s.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
    assert s.minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]) == 8
    assert s.minSubArrayLen(11, [1, 2, 3, 4, 5]) == 3
    assert s.minSubArrayLen(15, [1, 2, 3, 4, 5]) == 5


def test_solution():
    check_cases(Solution())
