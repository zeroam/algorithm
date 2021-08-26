from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for word in strings:
            chars = []
            for char in word:
                diff = ord(char) - ord(word[0])
                if diff < 0:
                    diff = diff + 26  # lower case count

                chars.append(diff)
            # print(f"{word}, {chars}")
            group[tuple(chars)].append(word)

        return group.values()


def _sort_items(items: List[List[str]]) -> List[List[str]]:
    return sorted([sorted(item) for item in items])


def check_cases(s: Solution):
    assert _sort_items(s.groupStrings(["a"])) == _sort_items([["a"]])
    assert _sort_items(
        s.groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
    ) == _sort_items([["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]])


def test_solution():
    check_cases(Solution())
