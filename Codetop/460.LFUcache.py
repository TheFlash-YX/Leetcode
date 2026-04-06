from collections import defaultdict
from multiprocessing import dummy
from typing import Optional


class Node:
    def __init__(self, key=0, val=0):
        self.key=key
        self.value=val
        self.pre=None
        self.next=None
        self.freq=1

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.key_to_node={}
        def new_list():
            dummy=Node()
            dummy.next=dummy
            dummy.pre=dummy
            return dummy
        self.freq_to_dummy=defaultdict(new_list)

    # 删除一个节点（抽出一本书）
    def remove(self, node) -> None:
        node.pre.next=node.next
        node.next.pre=node.pre

    # 在链表头添加一个节点（把一本书放到最上面）
    def push_front(self, dummy: Node, node: Node) -> None:
        node.pre=dummy
        node.next=dummy.next
        node.pre.next=node
        node.next.pre=node

    def get_node(self, key: int) -> Optional[Node]:
        if key not in self.key_to_node:  # 没有这本书
            return None
        node = self.key_to_node[key]  # 有这本书
        self.remove(node)  # 把这本书抽出来
        dummy = self.freq_to_dummy[node.freq]
        if dummy.prev == dummy:  # 抽出来后，这摞书是空的
            del self.freq_to_dummy[node.freq]  # 移除空链表
            if self.min_freq == node.freq:  # 这摞书是最左边的
                self.min_freq += 1
        node.freq += 1  # 看书次数 +1
        self.push_front(self.freq_to_dummy[node.freq], node)  # 放在右边这摞书的最上面
        return node



    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.value if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:  # 有这本书
            node.value = value  # 更新 value
            return
        if len(self.key_to_node) == self.capacity:  # 书太多了
            dummy = self.freq_to_dummy[self.min_freq]
            back_node = dummy.prev  # 最左边那摞书的最下面的书
            del self.key_to_node[back_node.key]
            self.remove(back_node)  # 移除
            if dummy.prev == dummy:  # 这摞书是空的
                del self.freq_to_dummy[self.min_freq]  # 移除空链表
        self.key_to_node[key] = node = Node(key, value)  # 新书
        self.push_front(self.freq_to_dummy[1], node)  # 放在「看过 1 次」的最上面
        self.min_freq = 1

