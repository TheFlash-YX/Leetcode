class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        self.result=[]
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
            used[i]=True
            path.append(nums[i])
            self.backtrack(nums,path,used)
            path.pop()
            used[i]=False
