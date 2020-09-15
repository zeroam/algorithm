from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n_start, n_end = newInterval
        
        merged = []
        inserted = False
        for start, end in intervals:
            if inserted:
                if n_end >= end:
                    continue
                elif start <= n_end < end:
                    merged[-1][1] = end
                    continue
            else:
                if n_start <= start:
                    if n_end < start:
                        merged.append([n_start, n_end])
                        inserted = True
                    elif n_end <= end:
                        start = n_start
                        inserted = True
                    elif n_end > end:
                        start = n_start
                        end = n_end
                        inserted = True
                        
                elif start < n_start <= end:
                    end = max(end, n_end)
                    inserted = True
                    
            merged.append([start, end])
            
        if not inserted:
            merged.append(newInterval)
            
        return merged


class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # init data
        n_start, n_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        
        # add all intervals starting before newInterval
        while idx < n and intervals[idx][0] < n_start:
            output.append(intervals[idx])
            idx += 1
            
        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < n_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], n_end)
            
        # add next intervals, merge with newInterval if needed
        while idx < n:
            start, end = intervals[idx]
            idx += 1
            
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append([start, end])
            # if there is an overlap, merge iwth the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
            
        return output


def check(intervals, new_intervals, expect):
    solutions = [s, s1]

    for solution in solutions:
        result = solution.insert(intervals, new_interval)
        print(f"comparing result: {result}, expect: {expect}", end=" ")
        assert result == expect
        print(f"passed!")


if __name__ == "__main__":
    s = Solution()
    s1 = Solution1()

    intervals = [[5, 7]]
    new_interval = [2, 3]
    expect = [[2, 3], [5, 7]]
    check(intervals, new_interval, expect)

    intervals = [[5, 7]]
    new_interval = [2, 6]
    expect = [[2, 7]]
    check(intervals, new_interval, expect)

    intervals = [[1, 2], [3, 5], [7, 8]]
    new_interval = [0, 9]
    expect = [[0, 9]]
    check(intervals, new_interval, expect)

    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 5]
    expect = [[1, 5], [6, 9]]
    check(intervals, new_interval, expect)

    intervals = [[1, 3], [6, 9]]
    new_interval = [2, 7]
    expect = [[1, 9]]
    check(intervals, new_interval, expect)
