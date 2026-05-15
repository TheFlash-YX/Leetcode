from typing import List


class Solution:
    # 时间复杂度O（mn）
    # 空间复杂度O（mn）
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for r, row in enumerate(matrix):
            for c, x in enumerate(row):
                if x == "1":
                    dp[r + 1][c + 1] = min(dp[r][c], dp[r + 1][c], dp[r][c + 1]) + 1

        return max(max(map,dp))**2



    # 时间复杂度O（mn）
    # 空间复杂度O（n）
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        max_side=0
        dp=[0]*(n+1)
        for i in range(m):
            pre=0
            for j in range(n):
                temp=dp[j+1]
                if matrix[i][j]=="1":
                    up=dp[j+1]
                    left=dp[j]
                    diag=pre
                    dp[j+1]=min(up,left,diag)+1
                    max_side=max(max_side,dp[j+1])
                else:
                    dp[j+1]=0
                pre=temp
            return max_side**2





Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])