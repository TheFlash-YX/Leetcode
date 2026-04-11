from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        min_tails = []

        for num in nums:
            pos = bisect_left(min_tails, num)
            if pos == len(min_tails):
                min_tails.append(num)
            else:
                min_tails[pos] = num

        return len(min_tails)



