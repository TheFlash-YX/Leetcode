import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:

        self.quick_sort(nums, 0, len(nums) - 1)
        return nums

    def quick_sort(self, nums: list[int], left: int, right: int) -> None:
        if left>=right:
            return

        ordered=True
        for i in range(left,right):
            if nums[i+1]<nums[i]:
                ordered=False
                break

        if ordered:
            return

        pivot_idx=self.partition(nums,left,right)
        self.quick_sort(nums,left,pivot_idx-1)
        self.quick_sort(nums,pivot_idx+1,right)


    def partition(self, nums: list[int], left: int, right: int) -> int:
        pivot_idx=random.randint(left,right)
        pivot=nums[pivot_idx]
        nums[left],nums[pivot_idx]=nums[pivot_idx],nums[left]

        i=left+1
        j=right

        while True:
            while i<=j and nums[i]<pivot:
                i+=1
            while i<=j and nums[j]>pivot:
                j-=1

            if i>j:
                break

            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

        nums[left],nums[j]=nums[j],nums[left]

        return j














