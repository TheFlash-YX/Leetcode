from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1<=nums[i]<=n and nums[nums[i]-1]!=nums[i]:
                target_index=nums[i]-1
                nums[i],nums[target_index]=nums[target_index],nums[i]

        for i in range(n):
            if nums[i]!=i+1:
                return i+1

        return n+1

nums=[1,2,0]
solution=Solution()
ans=solution.firstMissingPositive(nums)
print(ans)