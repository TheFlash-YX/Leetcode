# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d=0
        self.maxDepth(root)
        return self.max_d


    def maxDepth(self,node)->int:
        if not node:
            return 0
        left_depth=self.maxDepth(node.left)
        right_depth=self.maxDepth(node.right)
        self.max_d=max(self.max_d,left_depth+right_depth)

        return left_depth+right_depth+1

