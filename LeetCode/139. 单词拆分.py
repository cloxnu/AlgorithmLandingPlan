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
        queue = [0]
        

