from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[0]*(len(cost)+1)
        dp[0]=0
        dp[1]=0

        for i in range(2,len(cost)+1):
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

        return dp[len(cost)]

    def minCostClimbingStairs2(self, cost: List[int]) -> int:

        dp0=0
        dp1=0

        for i in range(2,len(cost)+1):
            dpi=min(dp1+cost[i-1],dp0+cost[i-2])
            dp0,dp1=dp1,dpi

        return dp1