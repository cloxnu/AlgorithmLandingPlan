from math import sqrt, floor


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(n+1):
            for j in range(1, floor(sqrt(i)) + 1):
                if i - j * j < 0:
                    break
                dp[i] = min(dp[i] if dp[i] != 0 else float('inf'), dp[i - j * j] + 1)
        return dp[n]
