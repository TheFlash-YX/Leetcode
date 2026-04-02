class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        map={}

        for idx,num in enumerate(nums):
            if target-num in map:
                return [idx,map[target-num]]
            else:
                map[num]=idx





