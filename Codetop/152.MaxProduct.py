class Solution:
    def maxproduct(self,nums:list[int])->int:
        dp0=dp1=1
        ans=nums[0]

        for x in nums:
            dp0,dp1=max(dp0*x,dp1,x),min(dp0*x,dp1*x,x)
            ans=max(ans,dp0)

        return ans