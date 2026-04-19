# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans=0
        self.dfs(root)
        return self.ans


    def dfs(self,node):
        if not node:
            return -1

        l_len=self.dfs(node.left)+1
        r_len=self.dfs(node.right)+1
        self.ans=max(self.ans,l_len+r_len)

        return max(l_len,r_len)
