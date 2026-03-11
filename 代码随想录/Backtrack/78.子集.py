from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.backtracking(nums,0,result,[])
        return result
    def backtracking(self,nums,startIndex,result,path):
        result.append(path[:])      # 收集子集，要放在终止添加的上面，否则会漏掉自己
        if startIndex>len(nums):
            result.apppend(path[:])
            return

        for i in range(startIndex,len(nums)):
            path.append(nums[i])
            self.backtracking(nums,i+1,result,path)
            path.pop()


