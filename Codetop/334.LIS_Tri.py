from bisect import bisect_left
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        min_tails = []

        for num in nums:
            pos = bisect_left(min_tails, num)
            if pos == 2:
                return True
            if pos == len(min_tails):
                min_tails.append(num)
            else:
                min_tails[pos] = num

        return False


