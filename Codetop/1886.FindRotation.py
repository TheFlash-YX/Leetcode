class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        for i in range(4):
            matrix=self.rotate(mat)
            if matrix==target:
                return True
        return False


    def rotate(self, matrix):
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for row in matrix:
            row.reverse()