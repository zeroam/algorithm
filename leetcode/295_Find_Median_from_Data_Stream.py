import bisect
import heapq


class MedianFinder:
    def __init__(self):
        self.nums = []
        self.is_sorted = False

    def addNum(self, num: int) -> None:
        self.nums.append(num)
        self.is_sorted = False

    def findMedian(self) -> float:
        if not self.is_sorted:
            self.nums.sort()
            self.is_sorted = True

        mid = len(self.nums) // 2
        if len(self.nums) % 2 == 0:  # even
            result = (self.nums[mid - 1] + self.nums[mid]) / 2
        else:
            result = self.nums[mid]

        return result


class MedianFinderBisect:
    def __init__(self):
        self.nums = []

    def _find_index(self, start: int, end: int, num: int):
        if start >= end:
            return start

        mid = (start + end) // 2
        if num < self.nums[mid]:
            return self._find_index(start, mid, num)
        else:
            return self._find_index(mid + 1, end, num)

    def addNum(self, num: int) -> None:
        idx = self._find_index(0, len(self.nums), num)
        self.nums.insert(idx, num)

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        if len(self.nums) % 2 == 0:  # even
            result = (self.nums[mid - 1] + self.nums[mid]) / 2
        else:
            result = self.nums[mid]

        return result


class MedianFinderBisect2:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.nums, num)

    def findMedian(self) -> float:
        mid = len(self.nums) // 2
        if len(self.nums) % 2 == 0:  # even
            result = (self.nums[mid - 1] + self.nums[mid]) / 2
        else:
            result = self.nums[mid]
        return result


class MedianFinderHeap:
    def __init__(self):
        self.low = []  # max-heap
        self.high = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.low) < len(self.high):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            result = -self.low[0]
        else:
            result = (-self.low[0] + self.high[0]) / 2
        return result


def check_cases(finder: MedianFinder):
    finder.addNum(12)
    assert finder.findMedian() == 12
    finder.addNum(10)
    assert finder.findMedian() == 11
    finder.addNum(13)
    assert finder.findMedian() == 12
    finder.addNum(11)
    assert finder.findMedian() == 11.5


def test_solution():
    check_cases(MedianFinder())


def test_solution_bisect():
    check_cases(MedianFinderBisect())


def test_solution_bisect2():
    check_cases(MedianFinderBisect2())


def test_solution_heap():
    check_cases(MedianFinderHeap())
