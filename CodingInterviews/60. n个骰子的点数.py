
# 递归解法
def dicesProbability(n: int) -> list:
    def dfs(s, i):
        if i == 1:
            if s in range(1, 7):
                return 1
            else:
                return 0
        return dfs(s - 1, i - 1) + dfs(s - 2, i - 1) + dfs(s - 3, i - 1) + dfs(s - 4, i - 1) + dfs(s - 5, i - 1) + dfs(s - 6, i - 1)
    value = {}
    res = []
    for j in range(n, 6 * n + 1):
        value[j] = dfs(j, n)
    for _, times in value.items():
        res.append(times / 6 ** n)
    return res


# 动态规划
def dicesProbability2(n: int) -> list:
    dp = [[0 for _ in range(6 * n)] for _ in range(n)]
    dp[0][0], dp[0][1], dp[0][2], dp[0][3], dp[0][4], dp[0][5] = 1, 1, 1, 1, 1, 1
    for i in range(1, n):
        for j in range(i, 6 * (i + 1)):
            dp[i][j] = (dp[i-1][j-1] if j-1 >= 0 else 0) + \
                (dp[i-1][j-2] if j-2 >= 0 else 0) + \
                (dp[i-1][j-3] if j-3 >= 0 else 0) + \
                (dp[i-1][j-4] if j-4 >= 0 else 0) + \
                (dp[i-1][j-5] if j-5 >= 0 else 0) + \
                (dp[i-1][j-6] if j-6 >= 0 else 0)
    res = []
    for i in range(n - 1, 6 * n):
        res.append(dp[n-1][i] / 6 ** n)
    return res


print(dicesProbability2(1))
