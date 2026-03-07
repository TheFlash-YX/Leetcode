# Definition for singly-linked list.
from turtledemo.penrose import star, start
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 1. 永远的保命符：虚拟头节点
        dummy = ListNode(0)
        dummy.next = head

        # pre 指针永远站在“即将要翻转的子链表”的正前方
        pre = dummy

        # 辅助函数：往前走 k 步，看看够不够人头
        def get_kth_node(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr

        while True:
            # 探子出发，找当前这组的第 k 个节点（也就是这组的尾巴）
            kth = get_kth_node(pre, k)

            # 如果探子扑空了，说明剩下的人数不够 k 个，直接下班！
            if not kth:
                break

                # 记录下一组的起始位置，防止走丢
            next_group = kth.next

            # 记录当前这组真实的起点（翻转后它会变成尾巴）
            start = pre.next

            # 🌟 核心魔法：局部翻转！
            # 和普通的翻转链表一模一样，只是 prev 初始化为 next_group，
            # 这样翻转完，第一块砖就自动连上了后面的大部队！
            prev = next_group
            curr = start

            # 只要 curr 还没走到下一组的领地，就继续翻转
            while curr != next_group:
                next_temp = curr.next  # 存下个节点
                curr.next = prev  # 掉头
                prev = curr  # prev 往前挪
                curr = next_temp  # curr 往前挪

            # 🌟 缝合伤口：把翻转好的这段，拼回主链表
            # 此时 kth 已经因为翻转跑到了最前面，成了新头
            pre.next = kth

            # pre 挪到这组的新尾巴上（也就是原来的 start），准备开启下一组的循环
            pre = start

        return dummy.next




