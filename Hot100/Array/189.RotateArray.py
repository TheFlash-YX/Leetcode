from typing import List
class Solution:
    #数组切片法，空间复杂度O(N)
    def rotate(self, nums: List[int], k: int) -> None:
        moves = k % len(nums)
        if moves==0:
            return
        nums[:] = nums[-moves:] + nums[:-moves]
    #三次翻转法，空间复杂度O(1)
    def rotate2(self, nums: List[int], k: int) -> None:
        k%=len(nums)
        if k==0:
            return

        def reverse(left:int,right:int)->None:
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)




nums=[1,2,3,4,5,6,7]
solution=Solution()
solution.rotate2(nums,3)
print(nums)