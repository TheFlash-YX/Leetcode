from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,0)
    def dfs(self, node, path_sum):
        if not node:
            return 0

        cur_sum=path_sum*10+node.val

        if not node.left and not node.right:
            return cur_sum

        left_sum=self.dfs(node.left,cur_sum)
        right_sum=self.dfs(node.right,cur_sum)

        return left_sum+right_sum


