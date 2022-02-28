import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for x, y in points:
            dist = x ** 2 + y ** 2
            min_heap.append((dist, [x, y]))
        heapq.heapify(min_heap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(min_heap)[1])

        return ans


def check_cases(s: Solution):
    s.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    s.kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]


def test_solution():
    check_cases(Solution())
