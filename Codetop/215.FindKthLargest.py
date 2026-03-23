import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap=nums[:k]
        heapq.heapify(min_heap)

        for i in range(k,len(nums)):
            if nums[i]>min_heap[0]:
                # 先弹出堆顶，再把新元素压入，内部只做一次调整
                heapq.heappushpop(min_heap,nums[i])

        return min_heap[0]













