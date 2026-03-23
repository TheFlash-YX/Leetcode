# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 递归，先序或后序遍历都可以
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right=root.right,root.left

        return root


    # 非递归，层次遍历
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue=deque()
        queue.append(root)

        while queue:
            node=queue.popleft()
            node.left,node.right=node.right,node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


        return root
