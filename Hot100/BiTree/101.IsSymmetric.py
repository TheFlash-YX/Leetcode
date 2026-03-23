# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 非递归，存镜像元组
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        que=deque()
        que.append((root.left,root.right))
        while que:
            left_node,right_node=que.popleft()
            if not left_node and not right_node:
                continue
            elif  not left_node or not right_node:
                return False
            elif left_node.val!=right_node.val:
                return False

            que.append((left_node.left,right_node.right))
            que.append((left_node.right,right_node.left))

        return True


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.check(root.left,root.right)


    def check(self,left_node,right_node):
        if not left_node and not right_node:
            return True
        elif not left_node or not right_node:
            return False
        elif left_node.val!=right_node.val:
            return False

        flag1=self.check(left_node.left,right_node.right)
        flag2=self.check(left_node.right,right_node.left)

        return flag1 and flag2

