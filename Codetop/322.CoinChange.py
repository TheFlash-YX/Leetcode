class Solution:
    # DP做法
    # 时间复杂度：O(n⋅amount)，其中 n 为 coins 的长度。
    # 空间复杂度：O(n⋅amount)。
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[[float('inf')]*(amount+1) for _ in range(len(coins)+1)]
        dp=[0][0]=0

        for i,coin in enumerate(coins):
            for j in range(amount+1):
                if coin>j:
                    dp[i+1][j]=dp[i][j]
                else:
                    dp[i+1][j]=min(dp[i][j],dp[i+1][j-coin]+1)

        ans=dp[-1][-1]
        return ans if ans!=float('inf') else -1


    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        ans = dp[-1]
        return ans if ans != float('inf') else -1

