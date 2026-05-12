from itertools import pairwise

class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: list[int]) -> int:
        special.sort()
        ans=max(special[0]-bottom,top-special[-1])
        for down,up in pairwise(special):
            ans=max(ans,up-down-1)

        return ans