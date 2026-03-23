# 1. 定义双向链表的节点
class DLinkedNode:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.pre=None
        self.next=None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache=dict()
        self.capacity=capacity
        self.head=DLinkedNode()
        self.tail=DLinkedNode()
        self.head.next=self.tail
        self.tail.pre=self.head

    def _add_node(self,node):
        node.pre=self.head
        node.next=self.head.next
        self.head.next.pre=node
        self.head.next=node

    def _remove_node(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre

    def _move_to_head(self,node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        node=self.tail.pre
        self._remove_node(node)
        return node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node=self.cache[key]
        self._move_to_head(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self._move_to_head(node)
        else:
            node=DLinkedNode(key,value)
            self._add_node(node)
            self.cache[key]=node
            if len(self.cache)>self.capacity:
                tail_node=self._pop_tail()
                del self.cache[tail_node.key]