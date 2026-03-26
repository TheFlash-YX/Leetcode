# class TreeNode:
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 层次遍历
    def rightSideView2(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []

        que=deque()
        ans=[]
        que.append(root)

        while que:
            length=len(que)
            for i in range(length):
                node=que.popleft()
                if i==length-1:
                    ans.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)


        return ans

    # 递归法
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        if not root:
            return []
        ans=[]
        self.dfs(root,0,ans)
        return ans

    def dfs(self,node,depth,ans):
        if not node:
            return

        if depth==len(ans):
            ans.append(node.val)

        self.dfs(node.right,depth+1,ans)
        self.dfs(node.left,depth+1,ans)




