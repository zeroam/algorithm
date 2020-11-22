from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        K = len(S)
        dp = [0] * K + [1]
        
        for i in range(K - 1, -1, -1):
            # Compute dp[i]

            for digit in digits:
                if digit < S[i]:
                    dp[i] += len(digits) ** (K - i - 1)
                elif digit == S[i]:
                    dp[i] += dp[i + 1]
                    
        return dp[0] + sum(len(digits) ** i for i in range(1, K))


if __name__ == "__main__":
    s = Solution()

    digits = ["1", "3", "5", "7"]
    n = 100
    expect = 20
    assert s.atMostNGivenDigitSet(digits, n) == expect

    digits = ["1", "3", "5", "7"]
    n = 15000
    expect = 468
    assert s.atMostNGivenDigitSet(digits, n) == expect

    digits = ["1", "3", "5", "7"]
    n = 20000
    expect = 596
    assert s.atMostNGivenDigitSet(digits, n) == expect