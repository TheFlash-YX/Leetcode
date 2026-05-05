class Solution:

    # 时间复杂度O（N）
    # 空间复杂度O（N）
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n

        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]

    # 时间复杂度O（N）
    # 空间复杂度O（1）
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n

        dp1=1
        dp2=2

        for i in range(3,n+1):
            dp=dp1+dp2
            dp1=dp2
            dp2=dp

        return dp



