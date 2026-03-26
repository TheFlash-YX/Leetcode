# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        length=len(nums)
        if length==0:
            return None

        return self.construct(0,length-1,nums)

    def construct(self,left,right,nums):
        if left>right:
            return None

        mid=(left+right)//2
        root=TreeNode(nums[mid])
        root.left=self.construct(left,mid-1,nums)
        root.right=self.construct(mid+1,right,nums)

        return root






