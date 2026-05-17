from typing import Optional



class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.pre=float("-inf")
        return self.inorder(root)

    def inorder(self,node):
        if not node:
            return True
        if not self.inorder(node.left):
            return False
        if self.pre<=node.val:
            return False

        self.pre=node.val
        return self.inorder(node.right)