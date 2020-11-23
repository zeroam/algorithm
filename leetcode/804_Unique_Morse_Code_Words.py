from typing import List

MORSE = [
    ".-",
    "-...",
    "-.-.",
    "-..",
    ".",
    "..-.",
    "--.",
    "....",
    "..",
    ".---",
    "-.-",
    ".-..",
    "--",
    "-.",
    "---",
    ".--.",
    "--.-",
    ".-.",
    "...",
    "-",
    "..-",
    "...-",
    ".--",
    "-..-",
    "-.--",
    "--..",
]


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        ret = set()
        for word in words:
            morse = ""
            for ch in word:
                morse += MORSE[ord(ch) - 97]

            ret.add(morse)

        return len(ret)


class SolutionOrigin:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        seen = {"".join(MORSE[ord(c) - ord('a')] for c in word) for word in words}

        return len(seen)


if __name__ == "__main__":
    s = Solution()
    s_o = SolutionOrigin()

    words = ["gin", "zen", "gig", "msg"]
    expect = 2
    assert s.uniqueMorseRepresentations(words) == expect
    assert s_o.uniqueMorseRepresentations(words) == expect
