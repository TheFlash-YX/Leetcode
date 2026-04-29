class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        ans=float('inf')
        cur_sum=0
        for right,num in enumerate(nums):
            cur_sum+=num
            while cur_sum>=target:
                ans=min(ans,right-left+1)
                cur_sum-=nums[left]
                left+=1

        return ans if ans < float('inf') else 0


