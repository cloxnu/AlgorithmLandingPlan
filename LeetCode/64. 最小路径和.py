class Solution:
    def minPathSum(self, grid: list) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = min(grid[i-1][j] if i-1 >= 0 else 0, grid[i][j-1] if j-1 >= 0 else 0) + grid[i][j]
        return grid[-1][-1]

