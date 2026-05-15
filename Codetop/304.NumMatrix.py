class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        sum = [[0] * (cols + 1) for _ in range(rows+1)]
        for r,row in enumerate(matrix):
            for c,n in enumerate(row):
                sum[r+1][c+1]=sum[r][c+1]+sum[r+1][c]-sum[r][c]+n
        self.sum=sum



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sum[row2+1][col2+1] - self.sum[row2+1][col1]-self.sum[row1][col2+1]+self.sum[row1][col1]


NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])