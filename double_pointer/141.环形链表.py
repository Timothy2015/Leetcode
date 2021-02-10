# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 双指针：快、慢双指针
        fast = head
        slow = head
        while fast!=None and fast.next!=None:
            fast = fast.next.next # 这个操作有意义，fast非空，fast.next非空
            slow = slow.next
            if fast == slow: 
                return True
        return False