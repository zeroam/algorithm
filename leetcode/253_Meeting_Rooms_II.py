import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort intervals by start
        intervals.sort()

        # add end to heap and compare min_end to next start
        count = 1
        min_heap = [intervals[0][1]]
        for start, end in intervals[1:]:
            min_end = min_heap[0]
            if start < min_end:
                count += 1
            else:
                heapq.heappop(min_heap)

            heapq.heappush(min_heap, end)

        return count


def check_cases(s: Solution):
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20], [22, 25], [13, 17], [7, 12], [6, 9]]) == 4


def test_solution():
    check_cases(Solution())
