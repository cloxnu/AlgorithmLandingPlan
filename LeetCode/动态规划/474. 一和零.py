class Solution:
    def findMaxForm(self, strs: list, m: int, n: int) -> int:
        dp = [[[0 for j in range(n+1)] for _ in range(m+1)] for _ in strs]
        for s in range(len(strs)):
            count0 = strs[s].count("0")
            count1 = len(strs[s]) - count0
            for i in range(m+1):
                for j in range(n+1):
                    dp[s][i][j] = dp[s-1][i][j] if s > 0 else 0
                    if i >= count0 and j >= count1:
                        dp[s][i][j] = max((dp[s-1][i][j] if s > 0 else 0), (dp[s-1][i-count0][j-count1] if s > 0 else 0) + 1)
        print(dp)
        print([dp[i][-1][-1] for i in range(len(strs))])
        return dp[-1][-1][-1]


solution = Solution()
print(solution.findMaxForm(['1001', '1110', '11', '000000', '001', '111111', '000000001', '1111110'], 9, 3))
