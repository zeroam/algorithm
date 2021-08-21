from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        for i, num in enumerate(nums):
            if num not in index_map:
                index_map[num] = i
                continue

            if i - index_map[num] <= k:
                return True

            index_map[num] = i

        return False


def check_cases(s: Solution):
    s.containsNearbyDuplicate([1, 2, 3, 1], 3) == True
    s.containsNearbyDuplicate([1, 0, 1, 1], 1) == True
    s.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2) == False
    s.containsNearbyDuplicate([1, 2, 3, 1, 1, 2, 3], 3) == True


def test_solution():
    check_cases(Solution())
