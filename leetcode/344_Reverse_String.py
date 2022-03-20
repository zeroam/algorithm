from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


class SolutionBuiltin:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


def check_cases(s: Solution):
    strings = ["h", "e", "l", "l", "o"]
    s.reverseString(strings)
    assert strings == ["o", "l", "l", "e", "h"]

    strings = ["H", "a", "n", "n", "a", "h"]
    s.reverseString(strings)
    assert strings == ["h", "a", "n", "n", "a", "H"]


def test_solution():
    check_cases(Solution())


def test_solution_builtin():
    check_cases(SolutionBuiltin())
