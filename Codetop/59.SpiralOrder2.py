class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        matrix = [[0] * n for _ in range(n)]
        row = col = di = 0
        dierctions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for i in range(n * n):
            matrix[row][col] = i + 1
            x, y = row + dierctions[di][0], col + dierctions[di][1]
            if x < 0 or x >= n or y < 0 or y >= n or matrix[x][y] != 0:
                di = (di + 1) % 4

            row += dierctions[di][0]
            col += dierctions[di][1]

        return matrix




