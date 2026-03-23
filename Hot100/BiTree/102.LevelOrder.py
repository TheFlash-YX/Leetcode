from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        que=deque()
        que.append(root)
        ans=[]
        while que:
            cur_len=len(que)
            cur_ans = []
            for i in range(cur_len):
                node=que.popleft()
                cur_ans.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

            ans.append(cur_ans)

        return  ans



