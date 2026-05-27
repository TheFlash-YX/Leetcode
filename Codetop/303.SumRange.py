class NumArray:
    def __init__(self, nums: list[int]):
        s=[0]*(len(nums)+1)
        for i,num in enumerate(nums):
            s[i+1]=s[i]+num
        self.s=s

    def sumRange(self, left: int, right: int) -> int:
        return self.s[right+1]-self.s[left]