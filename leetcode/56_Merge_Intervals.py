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


class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged_list = [intervals[0]]

        for cur_s, cur_e in intervals[1:]:
            prev_s, prev_e = merged_list[-1]
            if cur_s <= prev_e:
                if prev_e < cur_e:
                    merged_list[-1][1] = cur_e
            else:
                merged_list.append([cur_s, cur_e])
                
                
        return merged_list


def assert_test(intervals: List[List[int]], expect: List[List[int]]) -> None:
    assert s.merge(intervals) == expect
    assert s2.merge(intervals) == expect
        

if __name__ == "__main__":
    s = Solution()
    s2 = Solution2()

    intervals = [[1, 4], [0, 1]]
    expect = [[0, 4]]
    assert_test(intervals, expect)

    intervals = [[1, 4], [0, 4]]
    expect = [[0, 4]]
    assert_test(intervals, expect)

    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expect = [[1,6],[8,10],[15,18]]
    assert_test(intervals, expect)

    intervals = [[1,4],[4,5]]
    expect = [[1, 5]]
    assert_test(intervals, expect)

    intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    expect = [[1, 10]]
    assert_test(intervals, expect)
