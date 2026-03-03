from multiprocessing.connection import answer_challenge
from typing import List
import collections
class Solution:
    #枚举法
    def subarraySum1(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            cur_sum=0
            for j in range(i,-1,-1):
                cur_sum+=nums[j]
                if cur_sum==k:
                    ans+=1
        return ans

    #前缀和+哈希表优化
    def subarraySum2(self, nums: List[int], k: int) -> int:
        count=0
        pre=0
        mp=collections.defaultdict(int)
        mp[0]=1
        for i in range(len(nums)):
            pre+=nums[i]
            target=pre-k
            if target in mp:
                count+=mp[target]
            mp[pre]+=1

        return  count

if __name__=="__main__":
    solution=Solution()
    nums=[1,1,1]
    ans=solution.subarraySum2(nums,2)
    print(ans)