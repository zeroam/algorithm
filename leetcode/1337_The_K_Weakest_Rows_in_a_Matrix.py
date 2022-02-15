import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        powers = {}
        for i, row in enumerate(mat):
            powers[i] = 0
            for col in row:
                if col == 0:
                    break
                powers[i] += col

        heap = [(v, k) for k, v in powers.items()]
        heapq.heapify(heap)

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans


def check_cases(s: Solution):
    mat = [
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [1, 1, 1, 1, 1],
    ]
    k = 3
    s.kWeakestRows(mat, k) == [2, 0, 3]

    mat = [[1, 0, 0, 0], [1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0]]
    k = 2
    s.kWeakestRows(mat, k) == [0, 2]


def test_solution():
    check_cases(Solution())
