#给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result=[]
        path=[]
        self.backtracking(n,k,1,path,result)
        return result
    def backtracking(self,n,k,startindex,path,result):
        if len(path)==k:
            result.append(path[:])
            return

        for i in range(startindex,n-(k-len(path))+1+1):  #这里i的上限是剪枝优化后的结果
            path.append(i)
            self.backtracking(n,k,i+1,path,result)
            path.pop()
