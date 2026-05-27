from typing import List, Optional


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.result=[]
        self.dfs(root,[],targetSum)
        return self.result


    def dfs(self,node,path,target):
        if not node:
            return
        path.append(node.val)
        target-=node.val

        if not node.left and not node.right:
            if target==0:
                self.result.append(path[:])
        else:
            self.dfs(node.left,path,target)
            self.dfs(node.right,path,target)
        path.pop()


