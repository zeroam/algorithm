import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in range(k):
            heapq.heappush(min_heap, nums[i])

        for i in range(k, len(nums)):
            print(nums[i], min_heap[0])
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])

        return min_heap[0]


def check_cases(s: Solution):
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert s.findKthLargest([-1, 2, 0], 1) == 2


def test_solution():
    check_cases(Solution())
