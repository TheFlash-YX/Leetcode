
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right



class Solution:
    # 层次遍历/bfs
    def rightSideView1(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        que = deque()
        que.append(root)
        ans = []
        while que:
            cur_len = len(que)
            ans.append(que[-1].val)

            for _ in range(cur_len):

                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return ans

    # 深度优先遍历
    def rightSideView2(self, root: Optional[TreeNode]) -> list[int]:
        ans=[]

        def dfs(node,depth):
            if not node :
                return
            if len(ans)==depth:
                ans.append(node.val)

            dfs(node.right,depth+1)
            dfs(node.left,depth+1)

        dfs(root,0)
        return ans