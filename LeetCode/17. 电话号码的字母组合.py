def letterCombinations(digits: str) -> list:
    keyboard = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    res = []
    
    if len(digits) == 0: return []
    def dfs(s: str, idx: int, reduce: str):
        if idx >= len(s):
            res.append(reduce)
            return
        for value in keyboard[s[idx]]:
            dfs(s, idx + 1, reduce + value)
    
    dfs(digits, 0, "")
    return res


print(letterCombinations("27"))
