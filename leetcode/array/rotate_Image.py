class Solution:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # cách 1: pythoner
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[::] = zip(*matrix[::-1])

    # cách 2: hình học
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.reflect(matrix)
    
    def transpose(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reflect(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]
