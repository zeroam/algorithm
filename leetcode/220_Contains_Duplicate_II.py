from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        size = len(nums)
        # make list have index
        arr = [(num, i) for i, num in enumerate(nums)]
        arr.sort(key=lambda x: x[0])

        for i in range(0, size - 1):
            for j in range(i + 1, size):
                if abs(arr[i][0] - arr[j][0]) > t:
                    break

                if abs(arr[i][1] - arr[j][1]) <= k:
                    return True

        return False


class SolutionTimeLimitExeed:
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


def check_solution(nums: List[int], k: int, t: int, expect: bool):
    solutions: List[Solution] = [Solution(), SolutionTimeLimitExeed()]

    for s in solutions:
        assert s.containsNearbyAlmostDuplicate(nums, k, t) == expect


if __name__ == "__main__":
    check_solution([1, 2, 3, 1], 3, 0, True)
    check_solution([1, 0, 1, 1], 1, 2, True)
    check_solution([1, 5, 9, 1, 5, 9], 2, 3, False)
    check_solution([234, 235], 1, 100, True)
