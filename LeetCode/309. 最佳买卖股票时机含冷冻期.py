class Solution:
    def maxProfit(self, prices: list) -> int:
        if len(prices) == 0:
            return 0
        dp = [[0 for _ in range(3)] for i in prices]
        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
            dp[i][2] = dp[i-1][1] + prices[i]
            print(dp[i])

        return max(dp[-1][0], dp[-1][2])


