def longestValidParentheses(s: str) -> int:
    dp = [0 for _ in s]
    backetID = 1
    for l in range(1, len(s), 2):
        for i in range(0, len(s)):
            j = i + l
            if j >= len(s):
                break
            if s[i] == '(' and s[j] == ')':
                if l == 1 or dp[i + 1] == dp[j - 1]:
                    dp[i] = dp[j] = backetID
                    backetID += 1
    print(dp)
    longestTrueCount = 0
    count = 0
    for i in dp:
        if i != 0:
            count += 1
            longestTrueCount = max(longestTrueCount, count)
        else:
            count = 0
    return longestTrueCount

(()((()(()))(()()()(())(())())))))(((((()()(((()()(((((())))))(((())(
print(longestValidParentheses("(()()(()(()()(((()"))
# (()((()(()))(()()()(())(())())))))(((((()()(((()()(((((())))))(((())(
