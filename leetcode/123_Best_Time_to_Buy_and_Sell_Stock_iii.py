from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        left_min = prices[0]
        right_max = prices[-1]
        
        length = len(prices)
        left_profits = [0] * length
        right_profits = [0] * (length + 1)
        
        for l in range(1, length):
            left_profits[l] = max(left_profits[l - 1], prices[l] - left_min)
            left_min = min(left_min, prices[l])
            
            r = length - l - 1
            right_profits[r] = max(right_profits[r + 1], right_max - prices[r])
            right_max = max(right_max, prices[r])
            
        max_profit = 0
        for i in range(length):
            max_profit = max(max_profit, left_profits[i] + right_profits[i + 1])
            
        return max_profit


if __name__ == "__main__":
    s = Solution()

    case1 = [3, 3, 5, 0, 0, 3, 1, 4]
    assert s.maxProfit(case1) == 6

    case2 = [1, 2, 3, 4, 5]
    assert s.maxProfit(case2) == 4

    case3 = [7, 6, 4, 3, 1]
    assert s.maxProfit(case3) == 0
