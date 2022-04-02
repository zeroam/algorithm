class Solution:
    def reverse_array(self, start, end, array):
        while start < end:
            array[start], array[end] = array[end], array[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        output = [char for char in s]

        n = len(s)
        start, end = 0, 0
        while start < n:
            while end < n and output[end] != " ":
                end += 1

            self.reverse_array(start, end - 1, output)
            start = end + 1
            end += 1

        return "".join(output)


def check_cases(s: Solution):
    s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    s.reverseWords("God Ding") == "doG gniD"


def test_solution():
    check_cases(Solution())
