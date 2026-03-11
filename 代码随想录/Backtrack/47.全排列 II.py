from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        self.backtracking(nums,result,[],[False]*len(nums))
        return result

    def backtracking(self,nums,result,path,used):
        if len(path)==len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            #前半部分代表同一树层已经取过nums[i]这个数字了
            if (i >0 and nums[i]==nums[i-1] and not used[i-1]) or used[i]:
                continue

            path.append(nums[i])
            used[i]=True
            self.backtracking(nums,result,path,used)
            used[i]=False
            path.pop()