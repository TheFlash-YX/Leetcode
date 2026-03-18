class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]

        for i in range(1,len(nums)):
            dp[i]=max(nums[i],dp[i-1]+nums[i])

        return max(dp)

    def maxSubArray2(self, nums: list[int]) -> int:
        # 贪心算法 (卡登算法 Kadane's Algorithm) —— 最优空间解
        cur_sum=max_sum=nums[0]

        for i in range(1,len(nums)):
            cur_sum=max(nums[i],nums[i]+cur_sum)
            max_sum=max(cur_sum,max_sum)

        return max_sum
