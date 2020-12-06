def nthUglyNumber(n: int) -> int:
    dp = [1]
    a, b, c = 0, 0, 0
    while len(dp) < n:
        m = min(dp[a] * 2, dp[b] * 3, dp[c] * 5)
        if m == dp[a] * 2:
            a += 1
        elif m == dp[b] * 3:
            b += 1
        else:
            c += 1
        if m == dp[-1]: continue
        dp.append(m)
    print(dp)
    return dp[-1]
