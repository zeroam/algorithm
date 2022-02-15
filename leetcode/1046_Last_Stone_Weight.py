import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            num1 = heapq.heappop(max_heap)
            num2 = heapq.heappop(max_heap)
            diff = abs(num1 - num2)
            if diff > 0:
                heapq.heappush(max_heap, -1 * diff)

        if len(max_heap) == 0:
            return 0
        return -1 * max_heap[0]


def check_cases(s: Solution):
    assert s.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1
    assert s.lastStoneWeight([1]) == 1
    assert s.lastStoneWeight([2, 2]) == 0


def test_solution():
    check_cases(Solution())
