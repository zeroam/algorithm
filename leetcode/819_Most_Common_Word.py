import re
from collections import defaultdict, Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        d = defaultdict(int)

        words = re.findall("[a-zA-Z]+", paragraph)
        max_count = 0
        result = None
        for word in words:
            lower_word = word.lower()
            if lower_word in banned:
                continue

            d[lower_word] += 1
            if d[lower_word] > max_count:
                result = lower_word
                max_count = d[lower_word]

        return result


class SolutionCounter:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.findall(r"[\w]+", paragraph.lower())
        counter = Counter([word for word in words if word not in banned])
        return counter.most_common(1)[0][0]


def check_cases(s: Solution):
    assert (
        s.mostCommonWord(
            "Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]
        )
        == "ball"
    )
    assert s.mostCommonWord("a.", []) == "a"


def test_solution():
    check_cases(Solution())


def test_solution_counter():
    check_cases(SolutionCounter())
