class Solution:
    def myPow(self, x: float, n: int) -> float:
        ...


class SolutionRecursive(Solution):
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1
        return self.fastPow(x, n)

    def fastPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        half = self.fastPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x


class SolutionIterative:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1

        result = 1
        product = x
        while n != 0:
            if n % 2 == 1:
                result = result * product
            product = product * product
            n = n // 2

        return result


def check_cases(s: Solution):
    s.myPow(2, -2) == 1 / 4
    s.myPow(2, 0) == 1.0
    s.myPow(2, 2) == 4.0
    s.myPow(2, 10) == 1024.0


def test_solution_recursive():
    check_cases(SolutionRecursive())


def test_solution_iterative():
    check_cases(SolutionIterative())
