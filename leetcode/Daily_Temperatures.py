from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        days = [0] * size
        stack = [(temperatures[0], 0)]
        for i in range(size):
            cur_temp = temperatures[i]
            for j in range(len(stack) - 1, -1, -1):
                temp, index = stack[j]
                if cur_temp <= temp:
                    break
                days[index] = i - index
                stack.pop()

            stack.append((cur_temp, i))

        return days


def check_solutions(temperatures: List[int], expect: List[int]) -> None:
    s = Solution()

    assert s.dailyTemperatures(temperatures) == expect


if __name__ == "__main__":
    check_solutions([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])
    check_solutions([89, 62, 70, 58, 47, 47, 46, 76, 100, 70], [8, 1, 5, 4, 3, 2, 1, 1, 0, 0])
