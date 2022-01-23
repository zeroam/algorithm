from typing import List
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # make graph
        graph = defaultdict(set)
        indegree = dict()

        pre_word = words[0]
        for after_word in words[1:]:
            min_len = min(len(pre_word), len(after_word))
            for i in range(min_len):
                indegree.setdefault(pre_word[i], 0)
                indegree.setdefault(after_word[i], 0)

                if pre_word[i] != after_word[i]:
                    graph[pre_word[i]].add(after_word[i])
                    indegree[after_word[i]] += 1
                    break

            pre_word = after_word

        print(graph)
        print(indegree)
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
    assert s.alienOrder(["z", "x"]) == "zx"
    assert s.alienOrder(["z", "x", "z"]) == ""
    assert s.alienOrder(["ab", "adc"]) == "abcd"


def test_solution():
    check_cases(Solution())
