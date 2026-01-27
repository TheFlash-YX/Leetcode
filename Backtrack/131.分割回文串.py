from typing import List
class Solution:
    def backtracking(self,startIndex,s,result,path):
        if startIndex==len(s):
            result.append(path[:])

        for i in range(startIndex,len(s)):
            #优化判断回文函数
            if s[startIndex:i+1]==s[startIndex:i+1][::-1]:
                path.append(s[startIndex:i+1])
            else:
                continue
            self.backtracking(i+1,s,result,path)
            path.pop()




    def partition(self, s: str) -> List[List[str]]:
        result=[]
        self.backtracking(startIndex=0,s=s,result=result,path=[])
        return result