class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x

        while left+1<right:
            mid=(left+right)//2
            if mid*mid<=x:
                left=mid
            else:
                right=mid

        return left

Solution().mySqrt(4)