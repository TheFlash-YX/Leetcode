# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=0
        self.result=0
        self.inorder(root,k)
        return self.result

    def inorder(self,node,k):
        if not node or self.count>=k:
            return
        self.inorder(node.left,k)
        if self.count<k:
            self.result=node.val
            self.count+=1
        self.inorder(node.right,k)