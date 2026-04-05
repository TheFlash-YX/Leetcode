class Solution:
    # 贪心法
    def maxProfit1(self, prices: list[int]) -> int:
        ans=0

        for i in range(1,len(prices)):
            if prices[i-1]>=prices[i]:
                continue
            else:
                ans+=prices[i]-prices[i-1]

        return ans

    # 动态规划
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n)]
        dp[0][0]=0
        dp[0][1]=-prices[0]

        for i in range(1,n):
            for j in range(1):
                dp[i][0]=max(dp[i-1][0],dp[i-1][1]+prices[i])
                dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])

        return dp[n-1][0]