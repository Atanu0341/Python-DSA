

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Better approach
        n = len(matrix)
        m = len(matrix[0])

        row = [False] * n
        col = [False] * m

        # Mark rows and columns that contain zeros
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        # Zero out marked rows and columns
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0