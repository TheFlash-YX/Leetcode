from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum=sum(nums)
        if _sum%2 !=0:
            return False
        target=_sum//2

        dp=[0]*(target+1)

        for num in nums:
            for j in range(target,num-1,-1):
                dp[j]=max(dp[j],dp[j-num]+num)


        return dp[-1]==target
