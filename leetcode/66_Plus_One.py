from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        return [str(n) for n in str(num + 1)]


class SolutionCarry:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            digit = digits[i] + carry
            if digit == 10:
                digit = 0
                carry = 1
            else:
                carry = 0
            digits[i] = digit

        if carry:
            digits.insert(0, carry)
        return digits


def check_cases(s: Solution):
    s.plusOne([1, 2, 3]) == [1, 2, 4]
    s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    s.plusOne([9]) == [1, 0]


def test_solution():
    check_cases(Solution())


def test_solution_carry():
    check_cases(SolutionCarry())
