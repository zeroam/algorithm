class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s: str):
            return s == s[::-1]

        max_size = 1
        for i in range(len(s)):
            for j in range(i + max_size, len(s)):
                if is_palindrome(s[i:j + 1]):
                    max_size = j - i
                    result = s[i:j + 1]
        return result


class SolutionTwoPointers:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s)):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)
        return result
