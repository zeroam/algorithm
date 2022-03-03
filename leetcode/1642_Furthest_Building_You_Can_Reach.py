import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        prev = heights[0]

        total_jumps = 0
        largest_jumps = []
        largest_jumps_sum = 0
        complete = True
        for i, cur in enumerate(heights[1:]):
            diff = cur - prev
            prev = cur

            if diff <= 0:  # down or equal
                continue

            total_jumps += diff
            if len(largest_jumps) < ladders:
                heapq.heappush(largest_jumps, diff)
                largest_jumps_sum += diff
            elif largest_jumps and largest_jumps[0] < diff:
                largest_jumps_sum -= heapq.heappop(largest_jumps)
                largest_jumps_sum += diff

                heapq.heappush(largest_jumps, diff)

            # sum jumps, remaining largest r jumps
            if total_jumps - largest_jumps_sum > bricks:
                complete = False
                break

        return i + int(complete)


def check_cases(s: Solution):
    assert s.furthestBuilding([14, 3, 19, 3], 17, 0) == 3
    assert s.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4
    assert s.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7
    assert s.furthestBuilding([14, 3, 19, 3], 17, 0) == 3


def test_solution():
    check_cases(Solution())
