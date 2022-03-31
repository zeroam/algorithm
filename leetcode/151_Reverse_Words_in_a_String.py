import re


class Solution:
    def reverseWords(self, s: str) -> str:
        words = (x.group(0) for x in re.finditer(r"[\w]+", s))
        return " ".join(reversed(list(words)))


class SolutionStack:
    def reverseWords(self, s: str) -> str:
        stack = []
        result = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i] != " ":
                stack.append(s[i])
                continue

            if stack:
                result += " "
            while stack:
                result += stack.pop()
        if stack:
            result += " "
        while stack:
            result += stack.pop()

        return result.strip()


def check_cases(s: Solution):
    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world  ") == "world hello"
    assert s.reverseWords("a good  example") == "example good a"


def test_solution():
    check_cases(Solution())


def test_solution_stack():
    check_cases(SolutionStack())