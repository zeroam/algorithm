from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = []
        result = []
        
        def dfs(cnt: int, index: int, permu: List[int] = []) -> List[int]:
            if index >= n:
                if permu not in result:
                    result.append(permu)
                return
            
            for i in range(n):
                if i in used:
                    continue
                used.append(i)
                permu.append(nums[i])
                dfs(cnt + 1, index + 1, permu.copy())
                used.pop()
                permu.pop()
        
        dfs(0, 0)
        
        return result


class SolutionOrigin:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permuation
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return
            
            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1
                    
        backtrack([], Counter(nums))
        
        return results


if __name__ == "__main__":
    s = Solution()
    s_o = SolutionOrigin()

    nums = [1, 1, 2]
    expect = [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
    assert s.permuteUnique(nums) == expect
    assert s_o.permuteUnique(nums) == expect

    nums = [1, 2, 3]
    expect = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert s.permuteUnique(nums) == expect
    assert s_o.permuteUnique(nums) == expect
