from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_as = (int(char) for char in reversed(a))
        bin_bs = (int(char) for char in reversed(b))

        result = []
        carry = 0
        for bin_a, bin_b in zip_longest(bin_as, bin_bs, fillvalue=0):
            temp = bin_a + bin_b + carry
            carry, val = temp // 2, temp % 2
            result.insert(0, str(val))
        if carry:
            result.insert(0, str(carry))

        return "".join(result)


class SolutionParseInt:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"


def check_cases(s: Solution):
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"


def test_solution():
    check_cases(Solution())


def test_solution_parse_int():
    check_cases(SolutionParseInt())
