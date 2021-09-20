class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ans = 0
        for i, c1 in enumerate(s):
            substr = c1
            char_map = set([substr])
            for j in range(i + 1, len(s)):
                c2 = s[j]
                if c2 in char_map:
                    ans = max(ans, len(substr))
                    break

                char_map.add(c2)
                substr += c2

            ans = max(ans, len(substr))
        return ans


class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def check(start, end):
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return False
            return True

        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if check(i, j):
                    ans = max(ans, j - i + 1)

        return ans



class SolutionSlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0
        ans = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans


class SolutionMaxPointer:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        mp = {}

        i = 0
        for j, c in enumerate(s):
            if c in mp:
                i = max(mp[c], i)

            ans = max(ans, j - i + 1)
            mp[c] = j + 1

        return ans


def check_cases(s: Solution):
    assert s.lengthOfLongestSubstring("") == 0
    assert s.lengthOfLongestSubstring(" ") == 1
    assert s.lengthOfLongestSubstring("au") == 2
    assert s.lengthOfLongestSubstring("abcabcbb") == 3
    assert s.lengthOfLongestSubstring("bbbbb") == 1
    assert s.lengthOfLongestSubstring("kvrkd") == 4
    assert s.lengthOfLongestSubstring("pwwkew") == 3


def test_solution():
    check_cases(Solution())


def test_solution_brute_force():
    check_cases(SolutionBruteForce())


def test_solution_sliding_window():
    check_cases(SolutionSlidingWindow())


def test_solution_max_pointer():
    check_cases(SolutionMaxPointer())
