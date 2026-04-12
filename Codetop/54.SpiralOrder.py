from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dierctions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = []
        rows = len(matrix)
        cols = len(matrix[0])
        r = c = di = 0
        for _ in range(rows * cols):
            ans.append(matrix[r][c])
            matrix[r][c] = None
            x, y = r + dierctions[di][0], c + dierctions[di][1]

            if x < 0 or x >= rows or y < 0 or y >= cols or matrix[x][y] is None:
                di = (di + 1) % 4
            r += dierctions[di][0]
            c += dierctions[di][1]

        return ans


