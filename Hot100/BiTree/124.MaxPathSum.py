from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum=float('-inf')
        self.gain(root)
        return self.max_sum

    def gain(self,node)->int:
        if not node:
            return 0

        left_gain=max(self.gain(node.left),0)
        right_gain=max(self.gain(node.right),0)

        cur_sum=node.val+left_gain+right_gain
        self.max_sum=max(self.max_sum,cur_sum)

        return node.val+max(left_gain,right_gain)