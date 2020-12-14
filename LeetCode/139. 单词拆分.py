class Solution:
    def wordBreak(self, s: str, wordDict: list) -> bool:
        def dfs(idx):
            for word in wordDict:
                if idx >= len(s):
                    return True
                if idx + len(word) >= len(s):
                    continue
                if s[idx:idx+len(word)] == word:
                    dfs(idx + len(word))
        dfs(0)
        return False

    def wordBreak2(self, s: str, wordDict: list) -> bool:
        if len(s) == 0:
            return True
        dp = [False for _ in s] + [False]
        dp[0] = True
        for i in range(len(s)):
            for j in range(0, i+1):
                if dp[j]:
                    for word in wordDict:
                        if j+len(word) >= len(s)+1:
                            continue
                        if s[j:j+len(word)] == word:
                            dp[j+len(word)] = True
                            if j+len(word) == len(s):
                                return True

