class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)

        for i in range(n):
            while 0<=nums[i]<=n-1 and nums[nums[i]]!=nums[i]:
                j=nums[i]
                nums[i],nums[j]=nums[j],nums[i]

        for i in range(n):
            if nums[i]!=i:
                return i

        return n