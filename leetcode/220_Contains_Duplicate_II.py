from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        locs = set()
        # make all i, j
        for i in range(len(nums)):
            for dist in range(-k, k + 1):
                if dist == 0:
                    continue
                if i + dist < 0 or i + dist >= len(nums):
                    continue
                if (i + dist, i) in locs:
                    continue

                # check valid
                locs.add((i, i + dist))
                if abs(nums[i] - nums[i + dist]) <= t:
                    return True

        return False
