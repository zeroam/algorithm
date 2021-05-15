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


def check_solutions(ss: str, expect: bool):
    s = Solution()

    assert s.isValid(ss) == expect


if __name__ == "__main__":
    check_solutions("()[]{}", True)
    check_solutions("(", False)
    check_solutions(")", False)
    check_solutions("(())[]{([])}", True)
