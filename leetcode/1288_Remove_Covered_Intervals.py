from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        
        prev_e = 0
        for _, end in intervals:
            if end > prev_e:
                count += 1
                prev_e = end
                
        return count
        

if __name__ == "__main__":
    s = Solution()

    intervals = [[1, 4], [3, 6], [2, 8]]
    expect = 2
    assert s.removeCoveredIntervals(intervals) == expect

    intervals = [[1, 4], [2, 3]]
    expect = 1
    assert s.removeCoveredIntervals(intervals) == expect

    intervals = [[0, 10], [5, 12]]
    expect = 2
    assert s.removeCoveredIntervals(intervals) == expect

    intervals = [[3, 10], [4, 10], [5, 11]]
    expect = 2
    assert s.removeCoveredIntervals(intervals) == expect

    intervals = [[1, 2], [1, 4], [3, 4]]
    expect = 1
    assert s.removeCoveredIntervals(intervals) == expect
