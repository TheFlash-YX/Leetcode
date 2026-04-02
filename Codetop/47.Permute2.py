from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result=[]
        path=[]
        used=[False]*len(nums)
        self.backtrack(nums,[],used)
        return self.result

    def backtrack(self,nums,path,used):
        if len(path)==len(nums):
            self.result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            if i>0 and nums[i]==nums[i-1] and used[i-1]==False:
                continue

            used[i]=True
            path.append(nums[i])
            self.backtrack(nums,path,used)
            path.pop()
            used[i]=False


