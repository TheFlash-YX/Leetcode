from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que=deque()
        que.append([root,1])
        ans=0
        while que:
            cur_len=len(que)
            ans=max(ans,que[-1][1]-que[0][1]+1)
            for i in range(cur_len):
                node,idx=que.popleft()
                if node.left:
                    que.append([node.left,2*idx])
                if node.right:
                    que.append([node.right,2*idx+1])
        return ans
