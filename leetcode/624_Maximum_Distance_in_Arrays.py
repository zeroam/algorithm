from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_arrays = sorted(arrays, key=lambda x: x[0])
        min_value = min_arrays[0][0]
        max_value = -10001
        for i in range(1, len(arrays)):
            end = min_arrays[i][-1]
            if end > max_value:
                max_value = end
        result = max_value - min_value

        max_arrays = sorted(arrays, key=lambda x: x[-1], reverse=True)
        max_value = max_arrays[0][-1]
        min_value = 10001
        for i in range(1, len(arrays)):
            start = max_arrays[i][0]
            if start < min_value:
                min_value = start
        result = max(max_value - min_value, result)
        
        return result


class SolutionOn:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_value = arrays[0][0]
        max_value = arrays[0][-1]
        
        for i in range(1, len(arrays)):
            res = max(res, abs(max_value - arrays[i][0]), abs(arrays[i][-1] - min_value))
            
            min_value = min(min_value, arrays[i][0])
            max_value = max(max_value, arrays[i][-1])
            
        return res
        

if __name__ == "__main__":
    s = Solution()
    s_on = SolutionOn()

    arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]
    expect = 4
    assert s.maxDistance(arrays) == expect
    assert s_on.maxDistance(arrays) == expect
