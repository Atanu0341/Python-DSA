class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # Brute force
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    self.markRow(matrix, n, m, i)
                    self.markCol(matrix, n, m, j)

        for i in range(n):
            for j in range(m):
                if matrix[i][j] is None:
                    matrix[i][j] = 0
    
        return matrix

    def markRow(self, matrix, n, m, i):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = None

    def markCol(self, matrix, n, m, j):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = None
