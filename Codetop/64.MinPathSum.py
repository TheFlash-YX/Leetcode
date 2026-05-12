from typing import List


class Solution:
    # 空间复杂度O(m * n)
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == j == 1:
                    dp[1][1] = grid[0][0]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i - 1][j - 1]

        return dp[-1][-1]

    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp=[0]*n
        dp[0]=grid[0][0]

        for j in range(1,m):
            dp[j]=dp[j-1]+grid[0][j]

        for i in range(1,n):
            dp[0] = dp[0] + grid[i][0]

            for j in range(1, n):
                from_up = dp[j]
                from_left = dp[j - 1]
                dp[j] = min(from_up, from_left) + grid[i][j]

        return dp[n - 1]
