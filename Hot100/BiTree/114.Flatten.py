# Definition for a binary tree node.
from os import pread
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.pre=None
        self.reversePreorder(root)

    #逆先序遍历
    def reversePreorder(self,node)->None:
        if not node:
            return
        self.reversePreorder(node.right)
        self.reversePreorder(node.left)

        node.left=None
        node.right=self.pre
        self.pre=node

