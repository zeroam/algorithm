from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            res.append(max(nums[i: i + k]))
            
        return res


class SolutionDq:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()

        def clean_deque(i: int) -> None:
            if dq and dq[0] == i - k:
                dq.popleft()
                
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
                
            dq.append(i)
                
        res = []
        for i in range(k):
            clean_deque(i)
        res.append(nums[dq[0]]) 
        
        for i in range(k, len(nums)):
            clean_deque(i)
            res.append(nums[dq[0]])
        

        return res


def assert_solutions(nums: List[int], k: int, expect: List[int]) -> None:
    s = Solution()
    s_dq = SolutionDq()

    assert s.maxSlidingWindow(nums, k) == expect
    assert s_dq.maxSlidingWindow(nums, k) == expect


if __name__ == "__main__":
    assert_solutions([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7])
    assert_solutions([1], 1, [1])
    assert_solutions([1, -1], 1, [1, -1])
    assert_solutions([9, 11], 2, [11])
    assert_solutions([4, -2], 2, [4])
