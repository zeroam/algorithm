class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in map_s and map_s[char_s] != char_t:
                return False
            if char_t in map_t and map_t[char_t] != char_s:
                return False

            map_s[char_s] = char_t
            map_t[char_t] = char_s

        return True


def check_cases(s: Solution):

    assert s.isIsomorphic("egg", "add") == True
    assert s.isIsomorphic("foo", "bar") == False
    assert s.isIsomorphic("paper", "title") == True
    assert s.isIsomorphic("badc", "baba") == False


def test_solution():
    check_cases(Solution())
