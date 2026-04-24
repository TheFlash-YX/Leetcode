from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        que = deque()
        ans = []
        for i, num in enumerate(nums):
            while que and num > nums[que[-1]]:
                que.pop()
            que.append(i)

            if i - que[0] >= k:
                que.popleft()
            if i >= k - 1:
                ans.append(nums[que[0]])
        return ans





