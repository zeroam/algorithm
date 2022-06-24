from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char) :]
            if set(suffix) == set(s):
                return char + self.removeDuplicateLetters(suffix.replace(char, ""))

        return ""


class SolutionStack:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []

        for char in s:
            counter[char] -= 1
            if char in stack:
                continue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(char)

        return "".join(stack)


def check_cases(s: Solution):
    assert s.removeDuplicateLetters("bcab") == "bca"
    assert s.removeDuplicateLetters("bcabc") == "abc"
    assert s.removeDuplicateLetters("cbacdcbc") == "acdb"


def test_solution():
    check_cases(Solution())


def test_solution_stack():
    check_cases(SolutionStack())
