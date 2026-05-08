
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start=self.lower_bound(nums,target)
        if start==len(nums) or nums[start]!=target:
            return [-1,-1]
        end=self.lower_bound(nums,target+1)
        return[start,end-1]

    def lower_bound(self, nums, target):
        left=0
        right=len(nums)-1

        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1

        return left





