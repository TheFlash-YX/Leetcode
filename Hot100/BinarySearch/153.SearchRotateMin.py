from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right=0,len(nums)-1
        min_=float('inf')
        while left<=right:
            mid=(left+right)//2
            if nums[left]<=nums[mid]:
                min_=min(min_,nums[left])
                left=mid+1
            else:
                min_=min(min_,nums[mid])
                right=mid-1

        return min_