# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 时间复杂度：O(N2)，其中 n 为 preorder 的长度。最坏情况下二叉树是一条链，我们需要递归 O(n) 次，每次都需要 O(n) 的时间查找 preorder[0] 和复制数组。
    # 空间复杂度：O(N2)
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return

        root=TreeNode(val=preorder[0])
        idx=inorder.index(preorder[0])

        root.left=self.buildTree(preorder[1:idx+1],inorder[:idx])
        root.right=self.buildTree(preorder[idx+1:],inorder[idx+1:])

        return root


    # 哈希表优化
    # 时间复杂度O（N）
    # 空间复杂度O（N）
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        index={}
        for i,val in enumerate(preorder):
            index[val]=i

        def dfs(self,pre_l,pre_r,in_idx):
            if pre_l==pre_r:
                return

            left_size=index[preorder[pre_l]]-in_idx
            left=dfs(pre_l+1,pre_l+left_size,in_idx)
            right=dfs(pre_l+1+left_size,pre_l,in_idx+1+left_size)

            return TreeNode(preorder[pre_l],left,right)

        return dfs(0,len(preorder),0)









