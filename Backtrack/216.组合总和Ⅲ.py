from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.backtracking(0,n,[],result,k,1)
        return result
    def backtracking(self,currentsum,targetsum,path,result,k,startindex):
        if currentsum > targetsum:
            return
        if len(path)==k:
            if currentsum==targetsum:
                result.append(path[:])
            return

        for i in range(startindex,9):
            currentsum+=i
            path.append(i)
            self.backtracking(currentsum,targetsum,path,result,k,i+1)
            currentsum-=i
            path.pop()