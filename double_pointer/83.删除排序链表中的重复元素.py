# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 快慢双指针的变体
        slow = head; fast = head
        while fast:
            if fast.val != slow.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        if slow: slow.next = None
        return head