import re


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        match = re.search(needle, haystack)
        return match.start() if match else -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


def check_cases(s: Solution):
    assert s.strStr("hello", "ll") == 2
    assert s.strStr("aaaaa", "bba") == -1
    assert s.strStr("", "") == 0


def test_solution():
    check_cases(Solution())


def test_solution2():
    check_cases(Solution2())
