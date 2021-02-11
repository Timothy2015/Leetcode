# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 快慢双指针：如何寻找到倒数第n个节点？
        # 1.fast先走n步
        fast = head; slow = head
        for i in range(n):
            fast = fast.next
        ## 注意：fast有可能已经走到末尾了
        if fast==None:
            # 要删除的节点是第一个节点
            return head.next

        # 2.fast和slow再同速走，到fast到达链表末尾最后一个节点，slow.next指向的就是倒数第n个节点
        while fast.next:
            fast = fast.next
            slow = slow.next
        # 删除第n个节点
        slow.next = slow.next.next
        return  head