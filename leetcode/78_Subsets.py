from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(index: int, path: List[int]):
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])
        return result


def check_cases(s: Solution):
    assert sorted(s.subsets([1, 2, 3])) == sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert sorted(s.subsets([0])) == sorted([[], [0]])


def test_solution():
    check_cases(Solution())
