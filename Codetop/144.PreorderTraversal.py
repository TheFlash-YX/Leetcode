from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        self.ans=[]
        self.preorder(root)
        return self.ans
    def preorder(self,node):
        if not node:
            return
        self.ans.append(node.val)
        self.preorder(node.left)
        self.preorder(node.right)
