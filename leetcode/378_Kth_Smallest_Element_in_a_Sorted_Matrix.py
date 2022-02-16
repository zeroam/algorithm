import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count = 0
        size = len(matrix) * len(matrix[0])
        min_heap = []

        # find n - k + 1 th largest element
        for row in matrix:
            for col in row:
                if count < size - k + 1:
                    heapq.heappush(min_heap, col)
                    count += 1
                    continue

                if col > min_heap[0]:
                    heapq.heappush(min_heap, col)
                    heapq.heappop(min_heap)

        return min_heap[0]



def check_cases(s: Solution):
    s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
    s.kthSmallest([[-5]], 1) == -5


def test_solution():
    check_cases(Solution())
