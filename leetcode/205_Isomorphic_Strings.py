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


class SolutionIndexMapping:
    def mapping_index(self, s: str) -> str:
        mapper = {}
        new_str = []

        for i, c in enumerate(s):
            if c not in mapper:
                mapper[c] = i
            new_str.append(str(mapper[c]))

        return " ".join(new_str)

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.mapping_index(s) == self.mapping_index(t)


def check_cases(s: Solution):
    """
    requirements
    1. We can map a character only to itself or to one other character.
    2. No two character should map to same character
    3. Replacing each character in string 's' with the character it is mapped to results in string 't'
    """

    assert s.isIsomorphic("egg", "add") == True
    assert s.isIsomorphic("foo", "bar") == False
    assert s.isIsomorphic("paper", "title") == True
    assert s.isIsomorphic("badc", "baba") == False
    assert (
        s.isIsomorphic("abcdefghijklmnopqrstuvwxyzva", "abcdefghijklmnopqrstuvwxyzck")
        == False
    )


def test_solution():
    check_cases(Solution())


def test_solution_index_mapping():
    check_cases(SolutionIndexMapping())
