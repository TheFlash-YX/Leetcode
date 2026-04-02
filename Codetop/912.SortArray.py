import random


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def quick_sort(left,right):
            ordered=True
            for i in range(left,right):
                if nums[i]>nums[i+1]:
                    ordered=False
                    break

            if ordered:
                return

            pivot_idx=self.partition(left,right,nums)
            quick_sort(left,pivot_idx-1)
            quick_sort(pivot_idx+1,right)

        quick_sort(0,len(nums)-1)
        return nums


    def partition(self,left,right,nums):
        # 随机选取pivot，防止退化
        pivot_idx=random.randint(left,right)
        pivot=nums[pivot_idx]

        # pivot存在最左或最右
        nums[left],nums[pivot_idx]=nums[pivot_idx],nums[left]

        i=left+1
        j=right

        while True:
            # 找到需要交换的元素
            while i<=j and nums[i]<pivot:
                i+=1
            while i<=j and nums[j]>pivot:
                j-=1

            if i>=j:
                break
            # 交换元素
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

            # 为什么与 j 交换？
            # 如果与 i 交换，可能会出现 i = right + 1 的情况，已经下标越界了，无法交换
            # 另一个原因是如果 nums[i] > pivot，交换会导致一个大于 pivot 的数出现在子数组最左边，不是有效划分
            # 与 j 交换，即使 j = left，交换也不会出错

        nums[left],nums[j]=nums[j],nums[left]


        return j



