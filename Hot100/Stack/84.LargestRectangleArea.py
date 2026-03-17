from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        new_heights=[0]+heights+[0]
        stack=[]
        max_area=0

        for i in range(len(new_heights)):
            while stack and new_heights[i]<new_heights[stack[-1]]:
                mid_index=stack.pop()
                height=new_heights[mid_index]
                width=i-stack[-1]-1
                max_area=max(max_area,height*width)
            stack.append(i)

        return max_area
