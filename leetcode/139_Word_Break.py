from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 메모이제이션 활용
        def word_search(start: int, word: str, memo: list):
            if start == len(word):
                return True
            
            if memo[start] != None:
                return memo[start]
                
            for i in range(start + 1, len(word) + 1):
                if s[start:i] in wordDict and word_search(i, word, memo):
                    memo[start] = True
                    return memo[start]
                
            memo[start] = False
            return memo[start]
                    
        return word_search(0, s, [None] * len(s))


if __name__ == "__main__":
    s = Solution()

    word = "leetcode"
    word_dict = ["leet", "code"]
    assert s.wordBreak(word, word_dict) == True

    word = "applepenapple"
    word_dict = ["apple", "pen"]
    assert s.wordBreak(word, word_dict) == True

    word = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]
    assert s.wordBreak(word, word_dict) == False

    word = "aaaaaaaaaaaaaaab"
    word_dict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
    assert s.wordBreak(word, word_dict) == False

    word = "aaaaaaa"
    word_dict = ["aaa", "aaaa"]
    assert s.wordBreak(word, word_dict) == True
