# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        node_map={}
        cur=head
        while cur:
            node_map[cur]=Node(cur.val)
            cur=cur.next

        cur=head
        while cur:
            new_node=node_map[cur]
            # 使用 .get() 是因为如果 curr.next 是 None，字典找不到会返回 None，正好符合逻辑
            new_node.next=node_map.get(cur.next)
            new_node.random=node_map.get(cur.random)
            cur=cur.next

        return node_map[head]