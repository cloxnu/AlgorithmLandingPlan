def translateNum(num: int) -> int:
    def dfs(s: str, idx):
        if idx + 1 >= len(s):
            return 1
        if s[idx] == '1':
            return dfs(s, idx + 1) + dfs(s, idx + 2)
        if s[idx] == '2' and int(s[idx + 1]) <= 5:
            return dfs(s, idx + 1) + dfs(s, idx + 2)
        return dfs(s, idx + 1)
    return dfs(str(num), 0)

print(translateNum(12258))
