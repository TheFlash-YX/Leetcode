#接雨水
from gettext import dpgettext
from typing import List
class Solution:
    #动态规划
    def trap1(self, height: List[int]) -> int:
        leftMax=[0]*len(height)
        rightMax=[0]*len(height)
        leftMax[0]=height[0]
        rightMax[-1]=height[-1]

        for i in range(1,len(height)):
            leftMax[i]=max(leftMax[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i])

        dp=[0]*len(height)
        for i in range(len(height)):
            dp[i]=min(leftMax[i],rightMax[i])-height[i]

        return sum(dp)

    #双指针
    def trap2(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        ans_=0
        leftMax=rightMax=0
        while left<right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])
            if height[left]<height[right]:
                ans_+=leftMax-height[left]
                left+=1
            else:
                ans_+=rightMax-height[right]
                right-=1

        return ans






if __name__=="__main__":
    solution=Solution()
    height=[0,1,0,2,1,0,1,3,2,1,2,1]
    result=solution.trap2(height)
    print(result)