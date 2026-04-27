class Solution:
    # DP
    # 时间复杂度：O(nm)，其中 n 为 nums 的长度，m 为 nums 的元素和减去 ∣target∣
    # 空间复杂度：O(nm)
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        target+=sum(nums)
        if target<0 or target%2==1:
            return 0
        target = target // 2

        dp=[[0]*(target+1) for _ in range(len(nums)+1)]
        dp[0][0]=1

        for i,num in enumerate(nums):
            for j in range(target+1):
                if num>j:
                    dp[i+1][j]=dp[i][j]
                else:
                    dp[i+1][j]=dp[i][j]+dp[i][j-num]

        return dp[-1][-1]


    # 空间优化：用两个一维数组
    # 时间复杂度：O(nm)，其中 n 为 nums 的长度，m 为 nums 的元素和减去 ∣target∣
    # 空间复杂度：O(m)
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        target+=sum(nums)
        if target<0 or target%2==1:
            return 0
        target = target // 2
        dp=[[0]*(target+1) for _ in range(2)]
        dp[0][0]=1

        for i,num in enumerate(nums):
            for j in range(target+1):
                if num>j:
                    dp[(i+1)%2][j]=dp[i%2][j]
                else:
                    dp[(i+1)%2][j]=dp[i%2][j]+dp[i%2][j-num]

        return dp[len(nums)%2][-1]

    # 空间优化：用一个一维数组
    # 时间复杂度：O(nm)，其中 n 为 nums 的长度，m 为 nums 的元素和减去 ∣target∣
    # 空间复杂度：O(m)

    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        target+=sum(nums)
        if target<0 or target%2==1:
            return 0
        target = target // 2

        dp=[0]*(target+1)
        dp[0]=1

        for num in nums:
            for i in range(target,num-1,-1):
                dp[i]+=dp[i - num]


        return dp[-1]




