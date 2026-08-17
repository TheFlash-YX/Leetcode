from typing import Optional
class ListNode:
    def  __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class solution:
    # 迭代 o(n) o(1)
    def swapPairs(self,head:Optional[ListNode])->Optional[ListNode]:
        node0=dummy=ListNode(0,head)
        node1=head

        while node1 and node1.next:
            node2=node1.next
            node3=node2.next

            node0.next=node2
            node2.next=node1
            node1.next=node3

            node0=node1
            node1=node3

        return dummy.next

    # 递归 o（n）、o（n）
    def swapPairs(self,head:Optional[ListNode])->Optional[ListNode]:
        if not head or not head.next:
            return head

        node1=head
        node2=node1.next
        node3=node2.next

        node1.next=self.swapPairs(node3)
        node2.next=node1

        return node2
