# Definition for singly-linked list.
from typing import List,Optional
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy=ListNode(0)
        cur=dummy
        heap=[]

        for i,node in enumerate(lists):
            if node:
                heapq.heappush(heap,(node.val,i,node))

        while heap:
            val,i,min_node=heapq.heappop(heap)
            cur.next=min_node
            cur=cur.next
            if min_node.next:
                heapq.heappush(heap,(min_node.next.val,i,min_node.next))

        return dummy.next





