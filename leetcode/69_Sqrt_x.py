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


def check_cases(s: Solution):
    s.mySqrt(1) == 1
    s.mySqrt(4) == 2
    s.mySqrt(8) == 2
    s.mySqrt(9) == 3
    s.mySqrt(10) == 3


def test_solution():
    check_cases(Solution())
