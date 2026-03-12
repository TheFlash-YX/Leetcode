from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_dp=[0]*(len(nums))
        min_dp=[0]*(len(nums))
        max_dp[0]=nums[0]
        min_dp[0]=nums[0]

        for i in range(1,len(nums)):
            options=(nums[i],max_dp[i-1]*nums[i],min_dp[i-1]*nums[i])
            max_dp[i]=max(options)
            min_dp[i]=min(options)

        return max(max_dp)

