#盛最多水的容器
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=n-1
        current=0
        maxContent=0

        while left<right:
            current=min(height[left],height[right])*(right-left)
            maxContent=max(current,maxContent)
            if height[left]<=height[right]:
                left+=1
            else:
                right-=1

        return maxContent
