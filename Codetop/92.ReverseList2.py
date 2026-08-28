from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        p0=dummy
        pre=None
        for i in range(left-1):
            p0=p0.next
        cur=p0.next

        for i in range(right-left+1):
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp

        p0.next.next=cur
        p0.next=pre

        return dummy.next






head=ListNode(1)
node1=ListNode(2)
node2=ListNode(3)
node3=ListNode(4)
node4=ListNode(5)
head.next=node1
node1.next=node2
node2.next=node3
node3.next=node4
Solution().reverseBetween(head,2,4)
