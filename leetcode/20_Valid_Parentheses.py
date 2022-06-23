class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []
        for c in s:
            if c in pairs:
                stack.append(c)
            else:
                if len(stack) == 0 or c != pairs[stack[-1]]:
                    return False
                stack.pop()

        return len(stack) == 0


class Solution2:
    def isValid(self, s: str) -> bool:
        table = {")": "(", "]": "[", "}": "{"}
        stack = []
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack) == 0


def check_solutions(ss: str, expect: bool):
    s = Solution()

    assert s.isValid(ss) == expect


def check_cases(s: Solution):
    assert s.isValid("()[]{}") is True
    assert s.isValid("(") is False
    assert s.isValid(")") is False
    assert s.isValid("(())[]{([])}") is True


def test_solution():
    check_cases(Solution())


def test_solution2():
    check_cases(Solution2())
