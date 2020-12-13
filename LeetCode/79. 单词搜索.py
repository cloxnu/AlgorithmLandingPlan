class Solution:
    def exist(self, board: list, word: str) -> bool:
        visit = set()
        def dfs(i, j, idx) -> bool:
            if idx >= len(word):
                return True
            if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
                return False
            if (i, j) in visit:
                return False
            if board[i][j] == word[idx]:
                visit.add((i, j))
                try:
                    return dfs(i+1, j, idx+1) or dfs(i-1, j, idx+1) or dfs(i, j+1, idx+1) or dfs(i, j-1, idx+1)
                finally:
                    visit.remove((i, j))
            return False
        for a in range(len(board)):
            for b in range(len(board[0])):
                if board[a][b] == word[0]:
                    visit = set()
                    if dfs(a, b, 0):
                        return True
        return False

