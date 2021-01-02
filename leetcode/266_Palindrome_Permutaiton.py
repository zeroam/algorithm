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


class SolutionBruteForce:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0
        for i in range(0, 128 + 1):
            ct = 0
            for char in s:
                if ord(char) == i:
                    ct += 1

            count += ct % 2
        return count <= 1


class SolutionHashMap:
    def canPermutePalindrome(self, s: str) -> bool:
        hash_map = {}
        for char in s:
            hash_map.setdefault(char, 0)
            hash_map[char] += 1

        count = 0
        for cnt in hash_map.values():
            count += cnt % 2

        return count <= 1


class SolutionArray:
    def canPermutePalindrome(self, s: str) -> bool:
        char_map = [0] * 128
        for char in s:
            char_map[ord(char)] += 1

        count = 0
        for cnt in char_map:
            count += cnt % 2

        return count <= 1


class SolutionSinglePass:
    def canPermutePalindrome(self, s: str) -> bool:
        char_map = [0] * 128
        count = 0
        for char in s:
            char_map[ord(char)] += 1
            if char_map[ord(char)] % 2 == 0:
                count -= 1
            else:
                count += 1

        return count <= 1


class SolutionSet:
    def canPermutePalindrome(self, s: str) -> bool:
        char_set = set()
        for char in s:
            if char in char_set:
                char_set.remove(char)
            else:
                char_set.add(char)

        return len(char_set) <= 1


def check(s: str, expect: bool):
    solution = Solution()
    solution_bf = SolutionBruteForce()
    solution_hm = SolutionHashMap()
    solution_arr = SolutionArray()
    solution_sp = SolutionSinglePass()
    solution_s = SolutionSet()

    assert solution.canPermutePalindrome(s) == expect
    assert solution_bf.canPermutePalindrome(s) == expect
    assert solution_hm.canPermutePalindrome(s) == expect
    assert solution_arr.canPermutePalindrome(s) == expect
    assert solution_sp.canPermutePalindrome(s) == expect
    assert solution_s.canPermutePalindrome(s) == expect


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

    s = "AaBb//a"
    expect = False
    check(s, expect)
