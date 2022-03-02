import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)

        result = 0
        while len(sticks) > 1:
            x = heapq.heappop(sticks)
            y = heapq.heappop(sticks)
            stick = x + y
            result += stick
            heapq.heappush(sticks, stick)

        return result


def check_cases(s: Solution):
    assert s.connectSticks([2, 4, 3]) == 14
    assert s.connectSticks([1, 8, 3, 5]) == 30
    assert s.connectSticks([5]) == 0
    assert s.connectSticks([3354,4316,3259,4904,4598,474,3166,6322,8080,9009]) == 151646


def test_solution():
    check_cases(Solution())
