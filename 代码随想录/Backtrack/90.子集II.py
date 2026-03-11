from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        self.backtracking(nums, 0, result, [])
        return result

    def backtracking(self, nums, startIndex, result, path):
        result.append(path[:])  # 收集子集，要放在终止添加的上面，否则会漏掉自己
        #利用递归的时候下一个startIndex是i+1而不是0去重
        # for i in range(startIndex, len(nums)):
        #     if i>startIndex and nums[i]==nums[i-1]:
        #         continue
        #     path.append(nums[i])
        #     self.backtracking(nums, i + 1, result, path)
        #     path.pop()

        #利用集合去重
        uset = set()
        for i in range(startIndex,len(nums)):
            if nums[i] in uset:
                continue
            uset.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums,i+1,result,path)
            path.pop()
