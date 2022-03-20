from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        while True:
            try:
                char = strs[0][i]
                for word in strs:
                    if word[i] != char:
                        return word[:i]
            except IndexError:
                return strs[0][:i]

            i += 1


class SolutionHorizontal:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs[1:]:
            while word.find(prefix) != 0:
                prefix = prefix[:-1]

        return prefix


class SolutionDivideNConquer:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self._longestCommonPrefix(strs, 0, len(strs) - 1)

    def _longestCommonPrefix(self, strs, l: int, r: int) -> str:
        if l == r:
            return strs[l]

        mid = (l + r) // 2
        lcp_left = self._longestCommonPrefix(strs, l, mid)
        lcp_right = self._longestCommonPrefix(strs, mid + 1, r)

        return commonPrefix(lcp_left, lcp_right)


def commonPrefix(left: str, right: str) -> str:
    min_value = min(len(left), len(right))
    for i in range(min_value):
        if left[i] != right[i]:
            return left[:i]
    return left[:min_value]


def check_cases(s: Solution):
    assert s.longestCommonPrefix([""]) == ""
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_solution():
    check_cases(Solution())


def test_solution_horizontal():
    check_cases(SolutionHorizontal())


def test_solution_divide_n_conquer():
    check_cases(SolutionDivideNConquer())
