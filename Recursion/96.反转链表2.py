# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:


        successor = None
            # 第一步：简化问题，先解决子问题
        """子问题：反转从位置1到n的链表，即使m=1"""
        # 函数里面定义函数——不就是“闭包”嘛！
        def reverseN(head, n):
            nonlocal successor
            # base case, 画示意图，需要保存n处的后继节点并返回
            if n==1: 
                successor = head.next
                return head

            last = reverseN(head.next, n-1)
            head.next.next = head
            head.next = successor

            return last


        if m==1:
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head

    
    
   
