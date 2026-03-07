# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count=0
        self.prefix_sum_map={0:1}
        self.dfs(root,0,targetSum)
        return self.count
    def dfs(self,node,current_sum,targetSum)->None:
        if not node:
            return
        current_sum+=node.val
        target_pre=current_sum-targetSum
        if target_pre in self.prefix_sum_map:
            self.count+=self.prefix_sum_map[target_pre]
        self.prefix_sum_map[current_sum]=self.prefix_sum_map.get(current_sum,0)+1

        self.dfs(node.left,current_sum,targetSum)
        self.dfs(node.right,current_sum,targetSum)

        self.prefix_sum_map[current_sum]-=1

