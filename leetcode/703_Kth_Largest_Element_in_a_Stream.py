import heapq
from typing import Type, List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []

        for i in range(len(nums)):
            self.add(nums[i])

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif self.min_heap[0] < val:
            heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, val)

        return self.min_heap[0]


def check_cases(cls: Type[KthLargest]):
    kth_largest = cls(3, [4, 5, 8 ,2])
    assert kth_largest.add(3) == 4
    assert kth_largest.add(5) == 5
    assert kth_largest.add(10) == 5
    assert kth_largest.add(9) == 8
    assert kth_largest.add(4) == 8


def test_solution():
    check_cases(KthLargest)
