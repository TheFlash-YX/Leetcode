# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans=[]
        self.inOrder(root,ans)
        for i in range(len(ans) - 1):
            if ans[i + 1] <= ans[i]:
                return False

        return True

    def inOrder(self,node,ans):
        if not node:
            return
        self.inOrder(node.left,ans)
        ans.append(node.val)
        self.inOrder(node.right,ans)
