class Solution:
    def decodeString(self, s: str = "") -> str:
        stack = []
        for c in s:
            if c == "]":
                word = ""
                while stack[-1] != "[":
                    word += stack.pop()

                stack.pop()  # remove [
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)

                #print(f"num: {num}, word: {word}")

                for _ in range(num):
                    for i in range(len(word) - 1, -1, -1):
                        stack.append(word[i])
            else:
                stack.append(c)

        return "".join(stack)


def check_solutions(string: str, expect: str) -> None:
    s = Solution()

    assert s.decodeString(string) == expect


if __name__ == "__main__":
    check_solutions("3[a]2[bc]", "aaabcbc")
    check_solutions("10[abc]", "abcabcabcabcabcabcabcabcabcabc")
    check_solutions("3[a2[bc]]", "abcbcabcbcabcbc")
