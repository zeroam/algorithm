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


class SolutionCustomComparator:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:k]


class SolutionMinHeap:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
        heapq.heapify(min_heap)
        return [heapq.heappop(min_heap)[1] for _ in range(k)]


class SolutionBinarySearch:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [self.get_dist(point) for point in points]
        remaining = [i for i in range(len(points))]

        ans = []
        low, high = 0, max(distances)
        while k:
            mid = (low + high) / 2
            closer, farther = self.split_distances(remaining, distances, mid)
            if len(closer) > k:
                high = mid
                remaining = closer
            else:
                k -= len(closer)
                ans.extend(closer)
                remaining = farther
                low = mid

        return [points[i] for i in ans]

    def split_distances(self, remaining, distances, mid):
        closer, farther = [], []
        for index in remaining:
            if distances[index] <= mid:
                closer.append(index)
            else:
                farther.append(index)
        return closer, farther

    def get_dist(self, point: List[int]):
        return point[0] ** 2 + point[1] ** 2


class SolutionQuickSelect:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            pivot_index = self.partition(left, right, points)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1

        return points[:k]

    def partition(self, left, right, points):
        pivot = self.choose_pivot(left, right, points)
        pivot_dist = self.squared_distance(pivot)

        while left < right:
            if self.squared_distance(points[left]) < pivot_dist:
                left += 1
            else:
                points[left], points[right] = points[right], points[left]
                right -= 1

        if self.squared_distance(points[left]) < pivot_dist:
            left += 1
        return left

    def choose_pivot(self, left, right, points):
        return points[(left + right) // 2]

    def squared_distance(self, point):
        return point[0] ** 2 + point[1] ** 2


def check_cases(s: Solution):
    s.kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    s.kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
    s.kClosest([[1, 3], [-2, 2], [2, -2]], 2) == [[-2, 2], [2, -2]]
    s.kClosest([[0, 1], [1, 0]], 2) == [[0, 1], [1, 0]]


def test_solution():
    check_cases(Solution())


def test_solution_custom_comparator():
    check_cases(SolutionCustomComparator())


def test_solution_min_heap():
    check_cases(SolutionMinHeap())


def test_solution_binary_search():
    check_cases(SolutionBinarySearch())


def test_solution_quick_select():
    check_cases(SolutionQuickSelect())

