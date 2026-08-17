from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_line(nums[1:]), self.rob_line(nums[:-1]))

    def rob_line(self, nums: List[int]) -> int:
        dp0 = dp1 = 0

        for i in range(len(nums)):
            dp0, dp1 = dp1, max(dp0 + nums[i], dp1)

        return dp1
