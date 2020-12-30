class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [0] * (2 * k + 1)

        for i in range(1, len(prices)):
            for j in reversed(range(1, (2 * k + 1))):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] - prices[i - 1]) if j % 2 == 0 else max(dp[j - 1], dp[j] + prices[i] - prices[i - 1])

        return max(dp)
