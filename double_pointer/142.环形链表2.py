# https://leetcode-cn.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 快慢双指针 -- fast和slow第一次相遇
        fast = head; slow = head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        # 无环，fast先走到None，返回-1
        if fast==None or fast.next==None:
            return None
        
        # 有环，fast=slow
        # * fast回到head走k-m步，速度降低为1；slow继续走k-m，在环入口处相遇
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return slow



"""下面是精简版"""
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None: return None

        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow