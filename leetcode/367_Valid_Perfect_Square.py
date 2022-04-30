class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True

        left, right = 1, num // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1

        return False


def check_cases(s: Solution):
    s.isPerfectSquare(1) == True
    s.isPerfectSquare(2) == False
    s.isPerfectSquare(4) == True
    s.isPerfectSquare(14) == False
    s.isPerfectSquare(16) == True


def test_solution():
    check_cases(Solution())
