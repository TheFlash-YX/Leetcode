class Solution:

    # 空间复杂度O（N）
    def maxProfit1(self, prices: list[int]) -> int:
        dp=[0]*len(prices)
        min_price=prices[0]
        for i in range(1,len(prices)):
            min_price=min(min_price,prices[i])
            dp[i]=prices[i]-min_price

        return max(dp)

    def maxProfit(self, prices: list[int]) -> int:
        ans=float('-inf')
        min_prices=prices[0]

        for i in range(len(prices)):
            # 先卖股票，再更新历史最低最低价格
            ans=max(ans,prices[i]-min_prices)
            min_prices=min(min_prices,prices[i])


        return ans

Solution().maxProfit1([3,3,5,0,1,3,4])