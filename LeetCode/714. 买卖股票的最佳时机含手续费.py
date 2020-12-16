class Solution:
    def maxProfit(self, prices: list, fee: int) -> int:
        dp = [[0 for _ in range(2)] for _ in range(prices)]

        dp[0][1] = -fee-prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][1] + prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] - prices[i] - fee, dp[i-1][1])

        return dp[-1][0]
