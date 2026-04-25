from typing import Optional
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right



class Solution:
    # 递归,时间复杂度O(N)，空间复杂度O(H)
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        self.ans = []
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.ans.append(node.val)
        self.dfs(node.right)

    # 非递归，建立二叉线索树
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        ans = []

        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right is not root:
                    pre = pre.right

                if not pre.right:
                    pre.right = root
                    root = root.left
                    continue

                pre.right = None

            ans.append(root.val)
            root = root.right

        return ans

