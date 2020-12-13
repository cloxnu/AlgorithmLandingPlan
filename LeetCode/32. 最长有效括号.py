# def longestValidParentheses(s: str) -> int:
#     dp = [0 for _ in s]
#     backetID = 1
#     for l in range(1, len(s), 2):
#         for i in range(0, len(s)):
#             j = i + l
#             if j >= len(s):
#                 break
#             if s[i] == '(' and s[j] == ')':
#                 if l == 1 or dp[i + 1] == dp[j - 1]:
#                     dp[i] = dp[j] = backetID
#                     backetID += 1
#     print(dp)
#     longestTrueCount = 0
#     count = 0
#     for i in dp:
#         if i != 0:
#             count += 1
#             longestTrueCount = max(longestTrueCount, count)
#         else:
#             count = 0
#     return longestTrueCount


def longestValidParentheses(s: str) -> int:
    dp = [0 for _ in s]
    m = 0
    for i in range(len(s)):
        if i == 0:
            continue
        elif s[i] == ')' and s[i-1] == '(':
            dp[i] = (dp[i-2] if i-2 >= 0 else 0) + 2
        elif s[i] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
            dp[i] = (dp[i-dp[i-1]-2] if i-dp[i-1]-2 >= 0 else 0) + dp[i-1] + 2
        m = max(m, dp[i])
    print(dp)
    return m


print(longestValidParentheses("((((()))))"))
# (()((()(()))(()()()(())(())())))))(((((()()(((()()(((((())))))(((())(
