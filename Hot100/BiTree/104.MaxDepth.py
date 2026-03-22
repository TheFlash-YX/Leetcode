# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 递归，自底向上
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        return max(left,right)+1

    # 层次遍历法求深度
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth=0
        queue=deque()
        queue.append(root)
        while  queue:
            cur_len=len(queue)
            for i in range(cur_len):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1

        return depth