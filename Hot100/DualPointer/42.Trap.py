#接雨水

from typing import List
class Solution:
    #动态规划
    def trap1(self, height: List[int]) -> int:
        leftMax=[0]*len(height)
        leftMax[0]=height[0]
        rightMax=[0]*len(height)
        rightMax[-1]=height[-1]

        for i in range(1,len(height)):
            leftMax[i]=max(leftMax[i-1],height[i])
        for i in range(len(height)-2,-1,-1):
            rightMax[i]=max(rightMax[i+1],height[i])

        dp=[0]*len(height)

        for i in range(len(height)):
            dp[i]=min(leftMax[i],rightMax[i])-height[i]

        return sum(dp)


if __name__=="__main__":
    solution=Solution()
    height=[4,2,0,3,2,5]
    result=solution.trap(height)
    print(result)