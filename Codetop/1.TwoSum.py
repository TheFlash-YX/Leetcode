class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map={}

        for idx,num in enumerate(nums):
            if target-num in num_map:
                return [idx,num_map[target-num]]
            else:
                num_map[num]=idx






