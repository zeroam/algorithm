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


class SolutionReverse:
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1
        # remove leading spaces
        while left <= right and s[left] == " ":
            left += 1

        # remove trailing spaces
        while left <= right and s[right] == " ":
            right -= 1

        output = []
        while left <= right:
            if s[left] != " ":
                output.append(s[left])
            elif output[-1] != " ":
                output.append(" ")
            left += 1

        return output

    def reverse_array(self, l: list, start: int, end: int):
        while start < end:
            l[start], l[end] = l[end], l[start]
            start, end = start + 1, end - 1

    def reverseWords(self, s: str) -> str:
        output = self.trim_spaces(s)
        self.reverse_array(output, 0, len(output) - 1)

        n = len(output)
        start, end = 0, 0
        while start < n:
            while end < n and output[end] != " ":
                end += 1
            self.reverse_array(output, start, end - 1)

            # move to next word
            start = end + 1
            end += 1

        return "".join(output)


def check_cases(s: Solution):
    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world  ") == "world hello"
    assert s.reverseWords("a good  example") == "example good a"


def test_solution():
    check_cases(Solution())


def test_solution_stack():
    check_cases(SolutionStack())


def test_solution_reverse():
    check_cases(SolutionReverse())
