from typing import List, Optional


class Solution:
    def _binarySearch(self, intervals: List[List[int]], target: int, start: int, end: int) -> Optional[int]:
        if start >= end:
            if intervals[start][0] >= target:
                return intervals[start][0]
            return None
            
        mid = (start + end) // 2
        if intervals[mid][0] < target:
            return self._binarySearch(intervals, target, mid + 1, end)
        else:
            return self._binarySearch(intervals, target, start, mid)
    
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1] * n
        
        start_dict = {}
        for i, (start, end) in enumerate(intervals):
            start_dict[start] = i
            
        intervals.sort(key=lambda x: x[0])
        
        for i in range(n):
            min_start = self._binarySearch(intervals, intervals[i][1], i, n - 1)
            ans[start_dict[intervals[i][0]]] = start_dict.get(min_start, -1)
                
        return ans
                

if __name__ == "__main__":
    s = Solution()

    case1 = [[1, 2]]
    expect1 = [-1]
    assert s.findRightInterval(case1) == expect1

    case2 = [[3, 4], [2, 3], [1, 2]]
    expect2 = [-1, 0, 1]
    assert s.findRightInterval(case2) == expect2

    case3 = [[1, 4], [2, 3], [3, 4]]
    expect3 = [-1, 2, -1]
    assert s.findRightInterval(case3) == expect3