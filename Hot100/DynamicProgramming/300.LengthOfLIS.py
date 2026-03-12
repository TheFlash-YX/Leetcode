from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)

        return max(dp)


if __name__ =="__main__":
    solution=Solution()
    nums=[0,1,0,3,2,3]
    ans=solution.lengthOfLIS(nums)
    print(ans)