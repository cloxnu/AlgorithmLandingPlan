class Solution:
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for s in strs:
            count0 = s.count('0')
            count1 = len(s) - count0
            for i in reversed(range(m+1)):
                for j in reversed(range(n+1)):
                    if i >= count0 and j >= count1:
                        dp[i][j] = max(dp[i][j], dp[i-count0][j-count1] + 1)

        return dp[-1][-1]

