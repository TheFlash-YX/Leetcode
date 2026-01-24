from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        self.backtracking([],result,k,startindex=1,currentsum=0,targetsum=n)
        return result
    def backtracking(self,path,result,k,startindex,currentsum,targetsum):
        if currentsum > targetsum:
            return
        if len(path)==k:
            if currentsum==targetsum:
                result.append(path[:])
            return

        for i in range(startindex,9-(k-len(path))+1+1):
            currentsum+=i
            path.append(i)
            self.backtracking(path,result,k,i+1,currentsum,targetsum)
            currentsum-=i
            path.pop()