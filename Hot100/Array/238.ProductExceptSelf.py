from typing import List
class Solution:
    #空间复杂度O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=right=ans=[0]*len(nums)

        for i in range(len(nums)):
            if i==0:
                left[i]=1
            else:
                left[i]=left[i-1]*nums[i-1]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                right[i]=1
            else:
                right[i]=right[i+1]*nums[i+1]

        for i in range(len(nums)):
            ans[i]=left[i]*right[i]

        return ans

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        ans[0]=1
        for i in range(1,len(nums)):
            ans[i]=ans[i-1]*nums[i-1]
        R=1
        for i in range(len(nums)-1,-1,-1):
            ans[i]=ans[i]*R
            R*=nums[i]
        return ans