from functools import cmp_to_key
class Solution:
    def maxGoodNumber(self, nums: list[int]) -> int:
        bin_nums=[]
        for num in nums:
            bin_nums.append(bin(num)[2:])
        bin_nums.sort(key=cmp_to_key(lambda a,b:int(b+a)-int(a+b)))
        bin_ans="".join(bin_nums)
        ans=int(bin_ans,2)
        print(ans)


Solution().maxGoodNumber([1,2,3])