from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left=0
        right=len(nums)-1
        cur=0

        while cur<=right:
            if nums[cur]==0:
                nums[cur],nums[left]=nums[left],nums[cur]
                left+=1
                cur+=1
            elif nums[cur]==2:
                nums[cur], nums[right] = nums[right], nums[cur]
                right-=1
            else:
                cur+=1

    def sortColors2(self, nums: List[int]) -> None:
        n0=n1=0
        for i in range(len(nums)):
            temp=nums[i]
            nums[i]=2
            if temp<2:
                nums[n1]=1
                n1+=1
            if temp<1:
                nums[n0]=0
                n0+=1



if __name__ == "__main__":
    solution=Solution()
    nums=[2,0,2,1,1,0]
    solution.sortColors2(nums)
    print(nums)
