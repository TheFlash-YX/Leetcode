class Solution:
    # 时间复杂度O（mn）
    # 空间复杂度O（mn）
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp=[[0]*(n+1) for _ in range(m+1)]
        dp[1][1]=1

        for i in range(1,m+1):
            for j in range(1,n+1):
                if i==j==1:
                    continue
                if obstacleGrid[i-1][j-1]==1:
                    dp[i][j]=0
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]


    # 时间复杂度O（mn）
    # 空间复杂度O（n）
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0

        m,n=len(obstacleGrid),len(obstacleGrid[0])
        dp=[0]*n
        dp[0]=1

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                elif j>0:
                    dp[j]=dp[j]+dp[j-1]

        return dp[-1]

