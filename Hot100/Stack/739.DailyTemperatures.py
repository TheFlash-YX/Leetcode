from turtledemo.sorting_animate import instructions1
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                prev_index=stack.pop()
                ans[prev_index]=i-prev_index
            stack.append(i)

        return ans

if __name__=="__main__":
    temperatures=[73,74,75,71,69,72,76,73]
    solution=Solution()
    ans=solution.dailyTemperatures(temperatures)
    print(ans)
