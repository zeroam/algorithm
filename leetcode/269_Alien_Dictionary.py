from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # make graph
        graph = defaultdict(set)
        indegree = dict({c: 0 for word in words for c in word})

        pre_word = words[0]
        for after_word in words[1:]:
            min_len = min(len(pre_word), len(after_word))
            for i in range(min_len):
                pre_char = pre_word[i]
                after_char = after_word[i]

                if pre_char != after_char:
                    if after_char not in graph[pre_char]:
                        graph[pre_char].add(after_char)
                        indegree[after_char] += 1
                    break
            else:
                if len(pre_word) > len(after_word):
                    return ""

            pre_word = after_word

        queue = deque([k for k, v in indegree.items() if v == 0])
        ans = []

        while queue:
            node = queue.popleft()
            for nei in graph[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)

            ans.append(node)

        return "".join(ans) if len(ans) == len(indegree) else ""


def check_cases(s: Solution):
    assert s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert s.alienOrder(["wrt", "wrf", "er", "ett", "rw"]) == "wertf"
    assert s.alienOrder(["z", "x"]) == "zx"
    assert s.alienOrder(["z", "x", "z"]) == ""
    assert s.alienOrder(["ab", "adc"]) == "abcd"
    assert s.alienOrder(["abc", "ab"]) == ""


def test_solution():
    check_cases(Solution())
