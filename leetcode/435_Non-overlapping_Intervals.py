import sys
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        ans = 0
        final_end = -sys.maxsize
        for start, end in intervals:
            if start < final_end:
                ans += 1
            else:
                final_end = end

        return ans


if __name__ == "__main__":
    s = Solution()
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(s.eraseOverlapIntervals(intervals))
