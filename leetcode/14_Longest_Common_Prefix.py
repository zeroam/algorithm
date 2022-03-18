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


def check_cases(s: Solution):
    assert s.longestCommonPrefix([""]) == ""
    assert s.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert s.longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_solution():
    check_cases(Solution())


def test_solution_horizontal():
    check_cases(SolutionHorizontal())
