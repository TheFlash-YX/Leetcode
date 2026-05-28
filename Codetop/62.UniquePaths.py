class Solution:
    # 时间复杂度O（mn）
    # 空间复杂度O（mn）
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[1][1]==1
        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==j==1:
                    continue
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m][n]

    # 时间复杂度O（mn）
    # 空间复杂度O（n）
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[1]*n

        for i in range(1,m):
            for j in range(1,n):
                dp[j]=dp[j]+dp[j-1]

        return dp[-1]


Solution().uniquePaths(3,2)