from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            count = 0
            for j in range(i + 1, len(temperatures)):
                count += 1
                if temperatures[j] > temperatures[i]:
                    result[i] = count
                    break

        return result


class SolutionStack:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                last = stack.pop()
                result[last] = i - last
            stack.append(i)

        return result


def check_cases(s: Solution):
    assert s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert s.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert s.dailyTemperatures([30, 60, 90]) == [1, 1, 0]


def test_solution():
    check_cases(Solution())


def test_solution_stack():
    check_cases(SolutionStack())
