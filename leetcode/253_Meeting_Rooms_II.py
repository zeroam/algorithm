import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort intervals by start
        intervals.sort()

        # add end to heap and compare min_end to next start
        free_rooms = [intervals[0][1]]
        for start, end in intervals[1:]:
            if start >= free_rooms[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, end)

        return len(free_rooms)


class SolutionChronologicalOrdering:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted(i[0] for i in intervals)
        end_times = sorted(i[1] for i in intervals)

        end_pt = 0
        rooms = 0
        for start in start_times:
            end = end_times[end_pt]
            if start < end:
                rooms += 1
            else:
                end_pt += 1

        return rooms


def check_cases(s: Solution):
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert s.minMeetingRooms([[7, 10], [2, 4]]) == 1
    assert s.minMeetingRooms([[0, 30], [5, 10], [15, 20], [22, 25], [13, 17], [7, 12], [6, 9]]) == 4


def test_solution():
    check_cases(Solution())


def test_solution_chronical_ordering():
    check_cases(SolutionChronologicalOrdering())
