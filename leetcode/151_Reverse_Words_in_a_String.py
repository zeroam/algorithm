import re


class Solution:
    def reverseWords(self, s: str) -> str:
        words = (x.group(0) for x in re.finditer(r"[\w]+", s))
        return " ".join(reversed(list(words)))


def check_cases(s: Solution):
    assert s.reverseWords("the sky is blue") == "blue is sky the"
    assert s.reverseWords("  hello world  ") == "world hello"
    assert s.reverseWords("a good  example") == "example good a"


def test_solution():
    check_cases(Solution())
