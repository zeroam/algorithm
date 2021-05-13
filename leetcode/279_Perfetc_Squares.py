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


def check_solution(n: int, expect: int) -> None:
    s = Solution()

    assert s.numSquares(n) == expect


if __name__ == "__main__":
    check_solution(1, 1)
    check_solution(2, 2)
    check_solution(4, 1)
    check_solution(12, 3)
    check_solution(13, 2)
