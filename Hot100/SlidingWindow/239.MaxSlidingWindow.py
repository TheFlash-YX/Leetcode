from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # 双端队列作为滑动窗口
        dq=deque()
        ans=[]

        for i in range(len(nums)):
            while dq and nums[i]>nums[dq[-1]]:
                dq.pop()

            dq.append(i)

            if dq[0]<=i-k:
                dq.popleft()

            if i>=k-1:
                ans.append(nums[dq[0]])

        return ans