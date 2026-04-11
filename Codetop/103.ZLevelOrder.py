# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        que = deque()
        ans = []
        que.append(root)
        flag = 1
        while que:
            cur = []
            cur_len = len(que)
            for _ in range(cur_len):
                node = que.popleft()
                cur.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            if flag % 2 == 0:
                cur.reverse()
            flag += 1
            ans.append(cur)
        return ans

Solution().zigzagLevelOrder()