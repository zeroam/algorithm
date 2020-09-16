class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1]) if words else 0


class Solution1:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end > 0 and s[end] == " ":
            end -= 1
        begin = end
        while begin >= 0 and s[begin] != " ":
            begin -= 1
            
        return end - begin


if __name__ == "__main__":
    s = Solution()
    s1 = Solution1()

    string = "Hello World"
    expect = 5
    assert s.lengthOfLastWord(string) == expect
    assert s1.lengthOfLastWord(string) == expect

    string = "a "
    expect = 1
    assert s.lengthOfLastWord(string) == expect
    assert s1.lengthOfLastWord(string) == expect

    string = ""
    expect = 0
    assert s.lengthOfLastWord(string) == expect
    assert s1.lengthOfLastWord(string) == expect
