import math
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        square = 1
        nums = []
        while square ** 2 <= n:
            nums.append(square)
            square += 1

        nums.sort(reverse=True)
        dq = deque([(0, 0)])
        while dq:
            cur_total, depth = dq.popleft()
            for num in nums:
                total = cur_total + num ** 2
                if total < n:
                    dq.append((total, depth + 1))
                elif total == n:
                    return depth + 1


class SolutionBruteForce:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        def minNumSquares(k):
            if k in square_nums:
                return 1
            min_num = float("inf")

            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k - square) + 1
                min_num = min(min_num, new_num)

            return min_num

        return minNumSquares(n)


class SolutionDynamicProgramming:
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]

        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


class SolutionEnumeration:
    def numSquares(self, n: int) -> int:
        def is_divided_by(n: int, count: int) -> bool:
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i ** 2 for i in range(1, int(math.sqrt(n)) + 1)])

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count


class SolutionBFS:
    def numSquares(self, n: int) -> int:
        # list of square numbers that are less than `n`
        square_nums = [i * i for i in range(1, int(n ** 0.5) + 1)]

        level = 0
        queue = {n}
        while queue:
            level += 1
            #! Important: use set() instead of list() to eliminate the redundancy,
            # which would even provide a 5-times speedup, 200ms vs 1000ms
            next_queue = set()
            # construct the queue for the next level
            for remainder in queue:
                for square_num in square_nums:
                    if remainder == square_num:
                        return level
                    elif remainder < square_num:
                        break
                    else:
                        next_queue.add(remainder - square_num)
            queue = next_queue
        return level


def check_solution(n: int, expect: int) -> None:
    solutions = [
        Solution(),
        SolutionBruteForce(),
        SolutionDynamicProgramming(),
        SolutionEnumeration(),
        SolutionBFS(),
    ]

    for s in solutions:
        assert s.numSquares(n) == expect


if __name__ == "__main__":
    check_solution(1, 1)
    check_solution(2, 2)
    check_solution(4, 1)
    check_solution(12, 3)
    check_solution(13, 2)
