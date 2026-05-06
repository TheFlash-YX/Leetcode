class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        self.result=[]
        nums.sort()
        self.backtrack(0,nums,[])
        return self.result

    
    def backtrack(self,index,nums,path):
        self.result.append(path[:])

        for i in range(index,len(nums)):
            if i> index and nums[i]==nums[i-1]:
                continue
            path.append(nums[i])
            self.backtrack(i+1,nums,path)
            path.pop()







