from typing import List


class Solution:
    # 整体二分
    # 时间复杂度 O（logmn）
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
    # 排除法
    # 时间复杂度O(m+n)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = n - 1

        while 0 <= row < m and 0 <= col < n:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False