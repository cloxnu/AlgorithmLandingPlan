class Solution:
    def rotate(self, matrix: list) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        for i in range(len(matrix) // 2):
            for j in range(i, len(matrix) - 1 - i):
                # 1, 3, 9, 7 = 7, 1, 3, 9
                matrix[i][j], matrix[j][-1-i], matrix[-1-i][-1-j], matrix[-1-j][i] = matrix[-1-j][i], matrix[i][j], matrix[j][-1-i], matrix[-1-i][-1-j]


if __name__ == '__main__':
    solution = Solution()
    matrix = [[5, 1, 9, 11],
              [2, 4, 8, 10],
              [13, 3, 6, 7],
              [15, 14, 12, 16]]
    solution.rotate(matrix)
    print(matrix)
