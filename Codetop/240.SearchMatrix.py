from typing import List


class Solution:
    # 时间复杂度 O(m + n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = n - 1

        while 0 <= row < m and 0 <= col < n:
            if matrix[row][col] == target:
                return True
            while 0 <= col < n and matrix[row][col] > target:
                col -= 1
            while 0 <= row < m and matrix[row][col] < target:
                row += 1

        return False

Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]],5)
