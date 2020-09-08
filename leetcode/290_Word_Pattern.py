class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_word = dict()
        for i, k in enumerate(pattern):
            map_word.setdefault(k, [])
            map_word[k].append(i)
        words = str.split()

        # 패턴 갯수가 일치하는 지 체크
        if len(pattern) != len(words):
            return False

        # 같은 패턴끼리 동일한 단어를 가지고 있는 지 체크
        for k, indexs in map_word.items():
            for i in range(len(indexs) - 1):
                if words[indexs[i]] != words[indexs[i + 1]]:
                    return False

        # 패턴끼리 다른 단어를 가지고 있는 지 체크
        if len(map_word.keys()) != len(set(words)):
            return False

        return True


class Solution1:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_char = dict()
        map_word = dict()
        words = str.split()

        if len(pattern) != len(words):
            return False

        for c, w in zip(pattern, words):
            if c not in map_char:
                if w in map_word:
                    return False

                map_char[c] = w
                map_word[w] = c

            elif map_char[c] != w:
                return False

        return True


class Solution2:
    def wordPattern(self, pattern: str, str: str) -> bool:
        map_word = dict()
        words = str.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(words)):
            c = pattern[i]
            w = words[i]

            char = f"char_{c}"
            word = f"word_{w}"

            if char not in map_word:
                map_word[char] = i
            if word not in map_word:
                map_word[word] = i

            if map_word[char] != map_word[word]:
                return False

        return True



if __name__ == "__main__":
    s = Solution()
    s1 = Solution1()
    s2 = Solution2()

    pattern = "abba"
    string = "dog cat cat dog"
    expect = True
    assert s.wordPattern(pattern, string) == expect
    assert s1.wordPattern(pattern, string) == expect
    assert s2.wordPattern(pattern, string) == expect

    pattern = "abba"
    string = "dog cat cat fish"
    expect = False
    assert s.wordPattern(pattern, string) == expect
    assert s1.wordPattern(pattern, string) == expect
    assert s2.wordPattern(pattern, string) == expect

    pattern = "aaaa"
    string = "dog cat cat dog"
    expect = False
    assert s.wordPattern(pattern, string) == expect
    assert s1.wordPattern(pattern, string) == expect
    assert s2.wordPattern(pattern, string) == expect

    pattern = "abba"
    string = "dog dog dog dog"
    expect = False
    assert s.wordPattern(pattern, string) == expect
    assert s1.wordPattern(pattern, string) == expect
    assert s2.wordPattern(pattern, string) == expect

    pattern = "abb"
    string = "dog cat cat dog"
    expect = False
    assert s.wordPattern(pattern, string) == expect
    assert s1.wordPattern(pattern, string) == expect
    assert s2.wordPattern(pattern, string) == expect
