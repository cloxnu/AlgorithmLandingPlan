def longestPalindrome(s: str) -> str:
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    largest = 0
    largestij = (0, 0)

    for l in range(len(s)):
        for i in range(len(s)):
            j = i + l
            if j >= len(s):
                break
            if i == j:
                dp[i][j] = 2
            elif j == i + 1 and s[i] == s[j]:
                dp[i][j] = 2
            elif j >= i + 2:
                dp[i][j] = dp[i+1][j-1] + 2 if dp[i+1][j-1] != 0 and s[i] == s[j] else 0

            if dp[i][j] > largest:
                largest = dp[i][j]
                largestij = i, j

    return s[largestij[0]:largestij[1]+1]


print(longestPalindrome("123321"))

