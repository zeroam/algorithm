import heapq
import bisect
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone_1 = heapq.heappop(max_heap)
            stone_2 = heapq.heappop(max_heap)
            if stone_1 != stone_2:
                heapq.heappush(max_heap, stone_1 - stone_2)

        return -1 * max_heap[0] if max_heap else 0


class SolutionBisect:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            stone_1 = stones.pop()
            stone_2 = stones.pop()
            if stone_1 != stone_2:
                bisect.insort(stones, stone_1 - stone_2)

        return stones[0] if stones else 0




def check_cases(s: Solution):
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([1]) == 1
    assert s.lastStoneWeight([2, 2]) == 0


def test_solution():
    check_cases(Solution())


def test_solution_bisect():
    check_cases(SolutionBisect())
