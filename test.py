import collections
from contextlib import nullcontext
from email.utils import decode_params
from importlib.util import set_package
from logging import NullHandler
from traceback import clear_frames
from typing import Optional, List, no_type_check_decorator
from collections import defaultdict

from pkg_resources import resource_listdir


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.pre=0
        self.travalsel(root)
        return root
    def travalsel(self,node):
        if node is None:
            return
        self.travalsel(node.right)
        node.val+=self.pre
        self.pre=node.val
        self.travalsel(node.left)
