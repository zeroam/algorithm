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


class SolutionMinHeap:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        ladders_allocation = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:  # down or equal
                continue

            heapq.heappush(ladders_allocation, diff)
            if len(ladders_allocation) <= ladders:
                continue

            bricks -= heapq.heappop(ladders_allocation)
            if bricks < 0:
                return i

        return len(heights) - 1


class SolutionMaxHeap:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        bricks_allocation = []
        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff <= 0:  # down or equal
                continue

            heapq.heappush(bricks_allocation, -diff)
            bricks -= diff
            if bricks >= 0:
                continue
            if ladders == 0:
                return i

            bricks += -heapq.heappop(bricks_allocation)
            ladders -= 1

        return len(heights) - 1


def check_cases(s: Solution):
    assert s.furthestBuilding([14, 3, 19, 3], 17, 0) == 3
    assert s.furthestBuilding([4, 2, 7, 6, 9, 14, 12], 5, 1) == 4
    assert s.furthestBuilding([4, 12, 2, 7, 3, 18, 20, 3, 19], 10, 2) == 7
    assert s.furthestBuilding([14, 3, 19, 3], 17, 0) == 3
    assert s.furthestBuilding([2, 7, 9, 12], 5, 1) == 3


def test_solution():
    check_cases(Solution())


def test_solution_min_heap():
    check_cases(SolutionMinHeap())


def test_solution_max_heap():
    check_cases(SolutionMaxHeap())
