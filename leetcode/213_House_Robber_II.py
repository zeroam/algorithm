from typing import List


class SolutionUnsolved:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        
        max_total = 0
        def traverse_houses(index: int, total: int = 0):
            if index >= n:
                #print(f"total: {total}, index: {index}")
                nonlocal max_total
                if total > max_total:
                    max_total = total
                return
            
            #print(f"index: {index}")
            total = total + nums[index]
            
            traverse_houses(index + 2, total)
            traverse_houses(index + 3, total)
        
        # index 1 포함, n - 1 까지
        traverse_houses(1, 0)
        traverse_houses(2, 0)
        # index 0 포함, n - 2 까지
        n = n - 1
        traverse_houses(0, 0)
        
        return max_total


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0 or nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        return max(self.rob_simple(nums[:-1]), self.rob_simple(nums[1:]))

    def rob_simple(self, nums: List[int]) -> int:
        t1 = 0
        t2 = 0
        for current in nums:
            temp = t1
            t1 = max(current + t2, t1)
            t2 = temp

        return t1


if __name__ == "__main__":
    s = Solution()

    nums = [2, 3, 2]
    expect = 3
    assert s.rob(nums) == expect

    nums = [1, 3, 1, 3, 100]
    expect = 103
    assert s.rob(nums) == expect

    nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    expect = 16
    assert s.rob(nums) == expect
