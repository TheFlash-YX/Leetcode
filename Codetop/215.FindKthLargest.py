import heapq
import random


class Solution:
    # 基于堆排序，时间复杂度NlogK
    def findKthLargest2(self, nums: list[int], k: int) -> int:
        # 前k个最大的数
        min_heap=nums[:k]
        heapq.heapify(min_heap)

        # 遇到更大的数字就放进堆里
        for i in range(k,len(nums)):
            if nums[i]>min_heap[0]:
                heapq.heappushpop(min_heap,nums[i])

        return min_heap[0]



    # 快速选择
    def findKthLargest(self, nums: list[int], k: int) -> int:
        left=0
        right=len(nums)-1
        target_idx=len(nums)-k
        while True:
            p=self.partition(nums,left,right)
            if p==target_idx:
                return nums[p]
            elif p<target_idx:
                left=p+1
            else:
                right=p-1

    def partition(self,nums,left,right):
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

            if i>=j:
                break

            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1

        nums[j],nums[left]=nums[left],nums[j]
        return j











