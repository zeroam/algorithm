class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = False
        if len(s) % 2 == 1:
            odd = True

        mapping = {}
        for char in s:
            mapping.setdefault(char, 0)
            mapping[char] += 1

        for cnt in mapping.values():
            if odd and cnt % 2 == 1:
                odd = False
            elif cnt % 2 == 1:
                return False

        return True


def check(s: str, expect: bool):
    solution = Solution()

    assert solution.canPermutePalindrome(s) == expect


if __name__ == "__main__":
    s = "code"
    expect = False
    check(s, expect)

    s = "aab"
    expect = True
    check(s, expect)

    s = "carerac"
    expect = True
    check(s, expect)
