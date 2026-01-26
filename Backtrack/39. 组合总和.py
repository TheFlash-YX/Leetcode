from typing import List
class Solution:
    def backtracking(self,startIndex,target,sum,candidates,result,path):
        if sum>target:
            return
        if sum==target:
            result.append(path[:])
            return
        for i in range(startIndex,len(candidates)):
            if sum+candidates[i]>target:
                break
            path.append(candidates[i])
            self.backtracking(i,target,sum+candidates[i],candidates,result,path)
            path.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates)==0:
            return []
        candidates.sort()
        result=[]
        self.backtracking(0,target,0,candidates,result,path=[])
        return result