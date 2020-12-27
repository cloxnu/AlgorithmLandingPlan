class Solution:
    def coinChange(self, coins: list, amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], dp[i - coin] + 1)

        print(dp)
        return dp[amount] if dp[amount] != float('inf') else -1


s = Solution()
print(s.coinChange([474,83,404,3], 264))

