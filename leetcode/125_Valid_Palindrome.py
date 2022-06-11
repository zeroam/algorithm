import re
from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = []
        for char in s:
            if char.isalnum():
                words.append(char.lower())

        return words == words[::-1]


class SolutionDeque:
    def isPalindrome(self, s: str) -> bool:
        words = deque()
        for char in s:
            if char.isalnum():
                words.append(char.lower())

        while len(words) > 1:
            if words.popleft() != words.pop():
                return False
        return True


class SolutionRegex:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)
        return s == s[::-1]


def check_cases(s: Solution):
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
    assert s.isPalindrome(" ") == True
    assert s.isPalindrome("0P") == False


def test_solution():
    check_cases(Solution())


def test_solution_deque():
    check_cases(SolutionDeque())


def test_solution_regex():
    check_cases(SolutionRegex())
