class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        for c in s:
            d.setdefault(c, 0)
            d[c] += 1
            
        answer = 0
        for v in d.values():
            answer += v // 2 * 2
            if answer % 2 == 0 and v % 2 == 1:
                answer += 1
                
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
