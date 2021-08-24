from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            hash_map[sorted_word].append(word)

        return list(hash_map.values())


def check_case(s: Solution, strs: List[str], expect: List[List[str]]):
    result = sorted([sorted(item) for item in s.groupAnagrams(strs)])
    expect = sorted([sorted(item) for item in expect])

    assert result == expect


def check_cases(s: Solution):
    check_case(s, [""], [[""]])
    check_case(s, ["", ""], [["", ""]])
    check_case(s, ["a"], [["a"]])
    check_case(s, ["ab", "ba"], [["ab", "ba"]])
    check_case(
        s,
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    )


def test_solution():
    check_cases(Solution())
