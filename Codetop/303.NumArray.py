class NumArray:
    def __init__(self,nums:list[int]):
        pre=[0]*(len(nums)+1)
        for i,num in enumerate(nums):
            pre[i+1]=pre[i]+num
        self.presum=pre

    def sumRange(self,left:int,right:int):
        return self.presum[right+1]-self.presum[left]
