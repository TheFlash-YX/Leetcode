from collections import defaultdict
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cnt=defaultdict(int)
        cnt[0]=1
        ans=s=0

        for x in nums:
            s+=x
            ans+=cnt[s-k]
            cnt[s]+=1

        return ans


Solution().subarraySum([1,2,3],3)