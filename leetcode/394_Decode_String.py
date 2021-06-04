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


class Solution2Stacks:
    def decodeString(self, s: str = "") -> str:
        cnt_stack = []
        str_stack = []
        cur_str = ""
        k = 0
        for ch in s:
            if ch.isdigit():
                k = 10 * k + int(ch)
            elif ch == "[":
                cnt_stack.append(k)
                str_stack.append(cur_str)
                k = 0
                cur_str = ""
            elif ch == "]":
                decoded_str = str_stack.pop()
                for _ in range(cnt_stack.pop()):
                    decoded_str += cur_str
                cur_str = decoded_str
            else:
                cur_str += ch

        return cur_str


class SolutionRecursive:
    def __init__(self):
        self.index = 0

    def decodeString(self, s: str = "") -> str:
        result = ""
        while self.index < len(s) and s[self.index] != "]":
            if s[self.index].isalpha():
                result += s[self.index]
                self.index += 1
            elif s[self.index].isdigit():
                k = 0
                while self.index < len(s) and s[self.index].isdigit():
                    k = k * 10 + int(s[self.index])
                    self.index += 1
                self.index += 1  # ignore [
                decoded_string = self.decodeString(s)
                self.index += 1  # ignore ]

                for _ in range(k):
                    result += decoded_string
        return result


def check_solutions(string: str, expect: str) -> None:
    s = Solution()
    s_2stacks = Solution2Stacks()

    assert s.decodeString(string) == expect
    assert s_2stacks.decodeString(string) == expect


if __name__ == "__main__":
    check_solutions("3[a]2[bc]", "aaabcbc")
    check_solutions("10[abc]", "abcabcabcabcabcabcabcabcabcabc")
    check_solutions("3[a2[bc]]", "abcbcabcbcabcbc")
    check_solutions("3[a2[b2[c]d]]", "abccdbccdabccdbccdabccdbccd")
