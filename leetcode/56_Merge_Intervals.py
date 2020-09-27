from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return list()
        
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]
        for i in range(1, len(intervals)):
            _, prev_e = merged_intervals[-1]
            next_s, next_e = intervals[i]
            
            if next_s <= prev_e:
                merged_intervals[-1][1] = max(prev_e, next_e)
            else:
                merged_intervals.append([next_s, next_e])
        
        return merged_intervals


if __name__ == "__main__":
    s = Solution()

    intervals = [[1, 4], [0, 1]]
    expect = [[0, 4]]
    assert s.merge(intervals) == expect

    intervals = [[1, 4], [0, 4]]
    expect = [[0, 4]]
    assert s.merge(intervals) == expect

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expect = [[1,6],[8,10],[15,18]]
    assert s.merge(intervals) == expect

    intervals = [[1,4],[4,5]]
    expect = [[1, 5]]
    assert s.merge(intervals) == expect
