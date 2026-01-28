
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result=[]
        self.backtracking(0,result,[],nums)
        return result

    def backtracking(self,startIndex,result,path,nums):
        if len(path)>=2:
            result.append(path[:])
        uset=set()
        for i in range(startIndex,len(nums)):
            if nums[i] in uset or (path and nums[i]<path[-1]):
                continue

            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(i+1,result,path,nums)
            path.pop()
