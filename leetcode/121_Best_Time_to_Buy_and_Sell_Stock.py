from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit


class SolutionMinValue:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = prices[0]

        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit


def check_cases(s: Solution):
    assert s.maxProfit([7, 5, 3, 2, 1]) == 0
    assert s.maxProfit([2, 1, 2, 3, 5, 6, 3]) == 5
    assert s.maxProfit([2, 2, 3, 7, 6, 1, 3]) == 5


def test_solution():
    check_cases(Solution())  # Time Limit Exceeded


def test_solution_min_value():
    check_cases(SolutionMinValue())
