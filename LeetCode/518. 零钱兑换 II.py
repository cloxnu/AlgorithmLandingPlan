class Solution:
    def change(self, amount: int, coins: list) -> int:
        dp = [0 for _ in range(amount + 1)]

        for i in range(amount + 1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] += 1 if i == coin else dp[i-coin]

        return dp[amount]
