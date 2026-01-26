from typing import List

from pkg_resources import resource_listdir


class Solution:
    def backtracking(self,target,sum,result,path,startIndex,candidates):
        if sum>target:
            return
        if sum==target:
            result.append(path[:])
            return

        for i in range(startIndex,len(candidates)):
            #表示纵向搜索时可以重复使用元素
            if i>startIndex and candidates[i]==candidates[i-1]:
                continue
            if sum+candidates[i]>target:
                break

            path.append(candidates[i])
            self.backtracking(target,sum+candidates[i],result,path,i+1,candidates)
            path.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        # 对数组进行排序可以在每一层横向搜索时去重
        candidates.sort()
        self.backtracking(target,sum=0,result=result,path=[],startIndex=0,candidates=candidates)
        return result
