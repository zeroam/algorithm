class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            before = mid ** 2
            after = (mid + 1) ** 2

            if after < x:
                left = mid + 1
            elif before > x:
                right = mid - 1
            elif after == x:
                return mid + 1
            else:
                return mid


class SolutionBuiltin:
    def mySqrt(self, x: int) -> int:
        return int(x ** 0.5)


class SolutionBinarySearch:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 2, x // 2
        while left <= right:
            mid = (left + right) // 2
            num = mid * mid
            if num > x:
                right = mid - 1
            elif num < x:
                left = mid + 1
            else:
                return mid

        return right


def check_cases(s: Solution):
    s.mySqrt(1) == 1
    s.mySqrt(4) == 2
    s.mySqrt(8) == 2
    s.mySqrt(9) == 3
    s.mySqrt(10) == 3


def test_solution():
    check_cases(Solution())


def test_solution_builtin():
    check_cases(SolutionBuiltin())


def test_solution_binary_search():
    check_cases(SolutionBinarySearch())
