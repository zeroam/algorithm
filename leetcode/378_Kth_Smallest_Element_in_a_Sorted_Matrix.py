import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count = 0
        size = len(matrix) * len(matrix[0])
        min_heap = []

        # find n - k + 1 th largest element
        for row in reversed(matrix):
            for col in reversed(row):
                if count < size - k + 1:
                    heapq.heappush(min_heap, col)
                    count += 1
                    continue

                if col > min_heap[0]:
                    heapq.heappush(min_heap, col)
                    heapq.heappop(min_heap)
                else:
                    break

        return min_heap[0]


class SolutionHeap:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        min_heap = []
        n = len(matrix)

        for row in range(n):
            heapq.heappush(min_heap, (matrix[row][0], row, 0))

        for _ in range(k):
            v, r, c = heapq.heappop(min_heap)
            if c != n - 1:  # end of row
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

        return v


class SolutionBinarySearch:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def count_less_equal(matrix, start, end):
            mid = (start + end) / 2
            count = 0

            smaller, larger = start, end
            for row in range(len(matrix)):
                for col in range(len(matrix[row])):
                    cur_num = matrix[row][col]
                    if cur_num > mid:
                        larger = min(cur_num, larger)
                        break

                    count += 1
                    smaller = max(cur_num, smaller)

            return count, smaller, larger

        start, end = matrix[0][0], matrix[-1][-1]
        while start < end:
            count, smaller, larger = count_less_equal(matrix, start, end)
            if count == k:
                return smaller
            elif count < k:
                start = larger
            else:
                end = smaller

        return start


def check_cases(s: Solution):
    s.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8) == 13
    s.kthSmallest([[-5]], 1) == -5


def test_solution():
    check_cases(Solution())


def test_solution_heap():
    check_cases(SolutionHeap())


def test_solution_binary_search():
    check_cases(SolutionBinarySearch())
