from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        self.backtrack("",0,0,ans,n)
        return ans

    def backtrack(self,cur_str,left_count,right_count,ans,n):
        if len(cur_str)==2*n:
            ans.append(cur_str)
            return

        if left_count<n:
            self.backtrack(cur_str+"(",left_count+1,right_count,ans,n)

        if right_count<left_count:
            self.backtrack(cur_str+")",left_count,right_count+1,ans,n)