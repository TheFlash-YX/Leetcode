class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.result = []
        self.backtrack(nums, 0, [])
        return self.result


        # 选或不选，适合01背包问题
    def backtrack1(self, nums, index, path):
        if index == len(nums):
            self.result.append(path[:])
            return

        self.backtrack1(nums, index + 1, path)
        path.append(nums[index])
        self.backtrack1(nums, index + 1, path)
        path.pop()

        # for循环，适合 组合、排列等问题
    def backtrack(self,nums,index,path):
        self.result.append(path[:])

        for i in range(index,len(nums)):
            path.append(nums[i])
            self.backtrack(nums,i+1,path)
            path.pop()