class Solution:
    def maxProfit(self, prices: list) -> int:
        min_cost = float('inf')
        max_profit = 0
        for p in prices:
            min_cost = min(min_cost, p)
            max_profit = max(max_profit, p - min_cost)
        return max_profit
