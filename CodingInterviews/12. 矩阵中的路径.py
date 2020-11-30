def exist(board: list[list[str]], word: str) -> bool:
    
    def dfs(center, word_idx) -> bool:
        if word_idx >= len(word): return True
        if center[0] >= len(board) or center[0] < 0: return False
        if center[1] >= len(board[center[0]]) or center[1] < 0: return False
        if center in visited:
            return False
        if board[center[0]][center[1]] != word[word_idx]:
            return False
        visited[center] = True
        return_val = dfs((center[0]+1, center[1]), word_idx+1) or \
        dfs((center[0], center[1]+1), word_idx+1) or \
        dfs((center[0], center[1]-1), word_idx+1) or \
        dfs((center[0]-1, center[1]), word_idx+1)

        del visited[center]
        return return_val

    
    if len(board) == 0: return False
    if len(board[0]) == 0: return False
    idxs = []
    visited = {}
    for i, row in enumerate(board):
        for j, one in enumerate(row):
            if one == word[0]:
                idxs.append((i, j))
    for idx in idxs:
        visited = {}
        if dfs(idx, 0):
            return True
    return False

# print(exist([['1', '2', '3'], ['1', '2', '3']], '12'))
print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEF"))
