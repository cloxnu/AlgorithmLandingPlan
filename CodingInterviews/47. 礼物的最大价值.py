
# dfs
def maxValue(grid: list) -> int:
    def dfs(value, x, y, maxX, maxY):
        if x >= maxX or y >= maxY:
            return value
        return max(dfs(value + grid[x][y], x, y + 1, maxX, maxY), dfs(value + grid[x][y], x + 1, y, maxX, maxY))
    if len(grid) == 0: return 0
    if len(grid[0]) == 0: return 0
    return dfs(0, 0, 0, len(grid), len(grid[0]))

print(maxValue([[4]]))

# 动态规划
def maxVal(grid: list) -> int:
    if len(grid) == 0: return 0
    if len(grid[0]) == 0: return 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = max(grid[i - 1][j] if i > 0 else 0, grid[i][j - 1] if j > 0 else 0) + grid[i][j]
    return grid[-1][-1]
