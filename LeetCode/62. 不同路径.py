class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        queue = [(0, 0)]
        while queue:
            x, y = queue.pop(0)
            if x >= m or y >= n:
                continue
            if x == m - 1 and y == n - 1:
                res += 1
                continue
            queue.append((x + 1, y))
            queue.append((x, y + 1))
        return res

    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [[1 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                dp[i][j] = (dp[i-1][j] if i-1 >= 0 else 0) + (dp[i][j-1] if j-1 >= 0 else 0) + 1
        return dp[-1][-1]

