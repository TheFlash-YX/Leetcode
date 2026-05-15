from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.getHeight(root)!=-1


    def getHeight(self,node):
        if not node:
            return 0

        left=self.getHeight(node.left)
        if left==-1:
            return -1
        right=self.getHeight(node.right)
        if right==-1 or abs(left-right)>1:
            return -1

        return max(left,right)+1
