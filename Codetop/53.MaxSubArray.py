from pkgutil import resolve_name


class Solution:
    # 空间复杂度O（1）
    def maxSubArray(self, nums: list[int]) -> int:
        dp=ans=nums[0]
        for x in nums[1:]:
            dp=max(dp+x,x)
            ans=max(dp,ans)
        return ans




    def maxSubArray2(self, nums: list[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=nums[0]

        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1],0)+nums[i]

        return max(dp)