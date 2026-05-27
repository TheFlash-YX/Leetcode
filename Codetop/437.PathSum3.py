from collections import defaultdict
from lib2to3.pgen2 import token
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans=0
        self.cnt=defaultdict(int)
        self.cnt[0]=1
        self.dfs(root,0,targetSum)
        return self.ans


    def dfs(self,node,s,targetSum):
        if not node:
            return
        s+=node.val

        self.ans+=self.cnt[s-targetSum]

        self.cnt[s]+=1
        self.dfs(node.left,s,targetSum)
        self.dfs(node.right,s,targetSum)
        self.cnt[s]-=1

