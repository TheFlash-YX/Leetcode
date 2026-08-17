from typing import List


class Solution:
    def findlength(self,nums1:list[int],nums2:list[int])->int:
        m,n=len(nums1),len(nums2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        ans=0

        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1]==nums2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=0
                ans= max(ans,dp[i][j])

        return ans


    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    f[i + 1][j + 1] = f[i][j] + 1
        return max(map(max, f))  # 所有 f[i][j] 的最大值

