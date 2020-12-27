class Solution:
    def maximalSquare(self, matrix: list) -> int:
        row = [0 for _ in matrix[0]]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                row[j] = row[j] + 1 if matrix[i][j] != "0" else 0
            left, right = [-1] * len(row), [len(row)] * len(row)
            square = 0
            stack = []
            for j in range(len(row)):
                while stack and row[stack[-1]] > row[j]:
                    idx = stack.pop()
                    right[idx] = j
                left[j] = stack[-1] if stack else -1
                stack.append(j)
            print(row, left, right)
            for j in range(len(row)):
                square = max(square, min((right[j] - left[j] - 1), row[j]) ** 2)
            res = max(res, square)
        return res

