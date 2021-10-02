from collections import defaultdict
from typing import List


class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.dict = dict()
        for word in dictionary:
            abbr = self._make_abbr(word)
            if abbr not in self.dict:
                self.dict[abbr] = set([word])
            else:
                self.dict[abbr].add(word)

    def _make_abbr(self, word):
        size = len(word)
        abbr = word
        if size > 2:
            abbr = f"{word[0]}{size - 2}{word[-1]}"

        return abbr


    def isUnique(self, word: str) -> bool:
        abbr = self._make_abbr(word)
        if abbr not in self.dict:
            return True
        if len(self.dict[abbr]) == 1 and word in self.dict[abbr]:
            return True
        return False


def assert_solution(
    Solution: ValidWordAbbr,
    intial: List[str],
    values: List[str],
    expect: List[bool],
):
    s = Solution(intial)
    for v, e in zip(values, expect):
        assert s.isUnique(v) == e


def check_cases(Solution: ValidWordAbbr):
    assert_solution(
        Solution,
        ["deer", "door", "cake", "card"],
        ["dear", "cart", "cane", "make", "cake"],
        [False, True, False, True, True],
    )
    assert_solution(
        Solution,
        ["deer", "door", "cake", "card"],
        ["dear", "door", "cart", "cake"],
        [False, False, True, True],
    )
    assert_solution(
        Solution,
        ["a", "a"],
        ["a"],
        [True],
    )


def test_solution():
    check_cases(ValidWordAbbr)
