from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # Greedy Algo:
    # 从下往上安装摄像头：跳过leaves这样安装数量最少，局部最优 -> 全局最优
    # 先给leaves的父节点安装，然后每隔两层节点安装一个摄像头，直到Head
    # 0: 该节点未覆盖
    # 1: 该节点有摄像头
    # 2: 该节点有覆盖
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        result=[0]
        if self.traversal(root,result)==0:
            result[0]+=1
        return result[0]

    def traversal(self,cur:TreeNode,result:List[int])->int:
        if not cur:
            return 2

        left=self.traversal(cur.left,result)
        right=self.traversal(cur.right,result)

        if left==2 and right==2:
            return 0
        elif left==0 or right==0:
            result[0]+=1
            return 1
        else:
            return 2






