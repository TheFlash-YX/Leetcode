from typing import List
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1

        if i>=0:
            for j in range(len(nums)-1,i,-1):
                if nums[j]>nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]
                    break

        left=i+1
        right=len(nums)-1
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1

