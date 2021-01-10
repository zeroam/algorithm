from collections import defaultdict, deque
from typing import List


# Time Limit Exceed
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # BFS
        dq = deque([(beginWord, [beginWord], 1)])
        while dq:
            word, used, res = dq.popleft()
            #print(word, used, res)
            if word == endWord:
                return res

            for w in wordList:
                if w in used:
                    continue

                # compare words
                cnt = 0
                for i in range(len(word)):
                    if word[i] != w[i]:
                        cnt += 1

                if cnt == 1:
                    used = used.copy()
                    used.append(w)
                    dq.append([w, used, res + 1])

        return 0


class SolutionBFS:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        L = len(beginWord)

        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)


        dq = deque([(beginWord, 1)])
        visited = {beginWord: True}
        while dq:
            cur_word, level = dq.popleft()

            for i in range(L):
                intermediate_word = cur_word[:i] + "*" + cur_word[i + 1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level + 1

                    if word not in visited:
                        visited[word] = True
                        dq.append((word, level + 1))

                all_combo_dict[intermediate_word] = []

        return 0


def check_solution(begin_word: str, end_word: str, word_list: List[str], expect: int):
    s = Solution()
    s_bfs = Solution()

    assert s.ladderLength(begin_word, end_word, word_list) == expect
    assert s_bfs.ladderLength(begin_word, end_word, word_list) == expect


if __name__ == "__main__":
    check_solution("hit", "cog", ["hot", "dot", "dog", "lot", "cog"], 5)
    check_solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"], 0)
