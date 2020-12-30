class Solution:
    def maxProfit(self, prices: list) -> int:
        dp = [0] * 5

        for i in range(1, len(prices)):
            for j in reversed(range(1, 5)):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] - prices[i - 1]) if j % 2 == 0 else max(dp[j - 1], dp[j] + prices[i] - prices[i - 1])
            print(dp)

        return max(dp[0], dp[2], dp[4])

    def maxProfit2(self, prices: list):
        dp = [[0 for _ in range(2)] for _ in range(3)]

        dp[0][1] = -prices[0]
        dp[1][0] = float('-inf')
        dp[1][1] = float('-inf')
        dp[2][0] = float('-inf')
        dp[2][1] = float('-inf')
        print(dp)

        for i in range(1, len(prices)):
            dp[0][0] = 0
            dp[0][1] = max(dp[0][1], dp[0][0] - prices[i])
            dp[1][0] = max(dp[1][0], dp[0][1] + prices[i])
            dp[1][1] = max(dp[1][1], dp[1][0] - prices[i])
            dp[2][0] = max(dp[2][0], dp[1][1] + prices[i])
            dp[2][1] = float('-inf')
            print(dp)
        return max(dp[1][0], dp[2][0], 0)


if __name__ == '__main__':
    so = Solution()
    print(so.maxProfit([3,3,5,0,0,3,1,4]))
