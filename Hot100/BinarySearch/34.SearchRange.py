from typing import  List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        leftBound=self.findbound(nums,target,True)
        if leftBound==-1:
            return [-1,-1]
        rightBound=self.findbound(nums,target,False)

        return [leftBound,rightBound]



    def findbound(self,nums,target,isFirst):
        left,right=0,len(nums)-1
        bound=-1
        while left<=right:
            mid=(left+right)//2
            if target==nums[mid]:
                bound=mid
                if isFirst:
                    right=mid-1
                else:
                    left=mid+1
            elif target<nums[mid]:
                right=mid-1
            elif target>nums[mid]:
                left=mid+1

        return bound