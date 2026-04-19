from turtledemo.penrose import inflatedart
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=int('-inf')
        self.dfs(root)
        return self.ans

    def dfs(self,node):
        if not node:
            return 0

        left=self.dfs(node.left)
        right=self.dfs(node.right)
        self.ans=max(self.ans,left+right+node.val)

        return max(max(left,right)+node.val,0)



