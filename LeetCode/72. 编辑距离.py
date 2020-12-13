# dp[i][j] = \
#     min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1, if s1[i] != s2[j] \
#     min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] - 1) + 1, if s1[i] == s2[j]
