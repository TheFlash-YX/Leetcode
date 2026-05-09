from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # 注意平衡二叉树是每一个子树都要平衡
        if not root:
            return True
        def dfs(node):
            if not node:
                return 0
            leftdeep=dfs(node.left)
            rightdeep=dfs(node.right)
            return max(leftdeep,rightdeep)+1
        if abs(dfs(root.left)-dfs(root.right))>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)