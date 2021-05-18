from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = {"+", "-", "*", "/"}
        stack = []

        for token in tokens:
            if token in exp:
                op = token
                b = stack.pop()
                a = stack.pop()

                stack.append(int(eval(f"{a}{op}{b}")))
            else:
                stack.append(token)

        return stack.pop()


def check_solutions(tokens: List[str], expect: int):
    s = Solution()

    assert s.evalRPN(tokens) == expect


if __name__ == "__main__":
    check_solutions(["2", "1", "+", "3", "*"], 9)
    check_solutions(["4", "13", "5", "/", "+"], 6)
    check_solutions(["10", "6", "9", "3", "+", "-11", "*", "/", "*", 17, "+", "5", "+"], 22)
