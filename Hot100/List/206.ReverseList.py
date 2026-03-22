from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        pre=None
        cur=head
        while cur:
            temp=cur.next
            cur.next=pre
            cur=temp
            pre=cur
        return pre

# 3. 构造链表 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4

Solution().reverseList(head)