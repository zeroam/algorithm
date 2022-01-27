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


class SolutionDFS:
    def alienOrder(self, words: List[str]) -> str:
        # make graph
        graph = defaultdict(set)
        for pre_word, after_word in zip(words, words[1:]):
            for pre_char, after_char in zip(pre_word, after_word):
                if pre_char != after_char:
                    if after_char not in graph[pre_char]:
                        graph[pre_char].add(after_char)
                    break
            else:
                if len(after_word) < len(pre_word):
                    return ""

        WHITE = 0
        GRAY = 1
        BLACK = 2

        ans = []
        visited = {c: WHITE for word in words for c in word}
        is_cycle = False

        def dfs(char):
            nonlocal is_cycle
            if is_cycle:
                return

            visited[char] = GRAY

            for after_char in graph[char]:
                if visited[after_char] == WHITE:
                    dfs(after_char)
                elif visited[after_char] == GRAY:
                    is_cycle = True

            visited[char] = BLACK
            ans.append(char)

        for char in visited:
            if visited[char] == WHITE:
                dfs(char)
            if is_cycle:
                return ""

        return "".join(ans[::-1])


class SolutionDFS2:
    def alienOrder(self, words: List[str]) -> str:
        # make graph
        reverse_adj_list = {c: [] for word in words for c in word}
        for pre_word, after_word in zip(words, words[1:]):
            for pre_char, after_char in zip(pre_word, after_word):
                if pre_char != after_char:
                    reverse_adj_list[after_char].append(pre_char)
                    break
            else:
                if len(after_word) < len(pre_word):
                    return ""

        output = []
        seen = {}

        def visit(node):
            if node in seen:
                return seen[node]

            seen[node] = False  # mark node as gray
            for next_node in reverse_adj_list[node]:
                result = visit(next_node)
                if not result:
                    return False

            seen[node] = True  # mark node as black
            output.append(node)
            return True

        if not all(visit(node) for node in reverse_adj_list):
            return ""
        return "".join(output)


def check_cases(s: Solution):
    assert s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]) == "wertf"
    assert s.alienOrder(["wrt", "wrf", "er", "ett", "rw"]) == "wertf"
    assert s.alienOrder(["z", "x"]) == "zx"
    assert s.alienOrder(["z", "x", "z"]) == ""
    assert s.alienOrder(["ac", "ab", "b"]) in ["cab", "acb"]
    assert s.alienOrder(["ab", "adc"]) in ["abcd", "cbda", "abdc"]
    assert s.alienOrder(["abc", "ab"]) == ""


def test_solution():
    check_cases(Solution())


def test_solution_dfs():
    check_cases(SolutionDFS())


def test_solution_dfs2():
    check_cases(SolutionDFS2())
