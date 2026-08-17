class Solution:
    def movezeroes(self,nums:list[int])->None:
        n=len(nums)
        slow=fast=0
        for fast in range(n):
            if nums[fast]!=0:
                nums[fast],nums[slow]=nums[slow],nums[fast]
                slow+=1
            fast+=1

        return nums