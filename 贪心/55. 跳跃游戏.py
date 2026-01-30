from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        i=0
        cover=0

        while i<=cover:
            cover=max(i+nums[i],cover)
            if cover>=len(nums)-1:
                return True
            i+=1

        return False


if __name__ == "__main__":
    nums=[0,2,3]
    solution=Solution()
    result=solution.canJump(nums)
    print(result)