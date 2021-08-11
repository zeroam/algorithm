from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)

        return False


def check_solution(s: Solution, nums: List[int], expect: bool):
    assert s.containsDuplicate(nums) == expect


def test_solution():
    s = Solution()

    check_solution(s, [1, 2, 3, 1], True)
    check_solution(s, [1, 2, 3, 4], False)
    check_solution(s, [1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
