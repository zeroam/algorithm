from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combination(index: int = 0, cands: List[int] = []):
            total = sum(cands)
            if total >= target:
                if total == target:
                    result.append(cands.copy())
                return

            for i in range(index, len(candidates)):
                cands.append(candidates[i])
                combination(i, cands)
                cands.pop()

        combination()
        return result


class SolutionDFS:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(csum: int, index: int = 0, path: List[int] = []):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target)
        return result


def check_cases(s: Solution):
    assert s.combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert s.combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert s.combinationSum([2], 1) == []


def test_solution():
    check_cases(Solution())


def test_solution_dfs():
    check_cases(SolutionDFS())
