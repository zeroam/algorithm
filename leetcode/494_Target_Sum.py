from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        size = len(nums)

        def dfs(index: int, total: int=0):
            if index == size:
                if total == target:
                    nonlocal ans
                    ans += 1
                return

            remained = sum(nums[index:])
            if total - remained > target or total + remained < target:
                return

            num = nums[index]
            dfs(index + 1, total + num)
            dfs(index + 1, total - num)

        dfs(0, 0)

        return ans


class SolutionMemoization:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        size = len(nums)
        memo = [{} for _ in range(size)]

        def calculate(index: int, total: int=0):
            if index == size:
                if total == target:
                    return 1
                return 0

            if memo[index].get(total) != None:
                return memo[index][total]

            add = calculate(index + 1, total + nums[index])
            sub = calculate(index + 1, total - nums[index])
            memo[index][total] = add + sub

            return memo[index][total]

        return calculate(0, 0)


def check_solutions(nums: List[int], target: int, expect: int):
    solutions = [Solution(), SolutionMemoization()]

    for s in solutions:
        assert s.findTargetSumWays(nums , target) == expect


if __name__ == "__main__":
    check_solutions([1], 1, 1)
    check_solutions([1, 1, 1, 1, 1], 3, 5)
