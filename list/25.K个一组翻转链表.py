# 题目：https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """ 递归 + 迭代 结合来解题 """

        # 迭代反转节点区间[a,b)之间的节点--这是和之前reverseN(head, n)不同的
        #  * 1. 这里n的值不容易获得，但是节点b容易获得
        #  * 2. b 为head迭代k次后的head.next
        def reverseInterval(a, b):
            # 暂时不需要考虑完整串接(pre的值)的问题，实现核心的反转即可
            pre = None; cur = a
            while cur != b:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            # 返回新的头节点
            return pre
        
        a = head; b = head
        for i in range(k):
            # base case : 不足k个节点，无法反转
            if b==None : return head # 为啥是head，因为head是当前反转区间的起点
            b = b.next
        newHead = reverseInterval(a, b) # 保存每一段区间[a, b)的新的头节点（头）
        # head.next = self.reverseKGroup(b, k) 
        a.next = self.reverseKGroup(b, k) # 尾部指向下一个反转区间（尾）
        return newHead
        
        
        """ 【只能使用常数的额外空间，则不能使用递归，只能迭代】
        # 基本子问题：给定头节点，如果翻转前n个节点
        successor = None
        def reverseN(head, n):
            # 使得闭包reverseN中successor和外部函数reverseKGroup中successor是同一变量
            nonlocal successor 

            if n==1:
                successor = head.next
                return head
            last = reverseN(head.next, n-1)
            head.next.next = head.next
            head.next = successor

            return last
        """
        """
        # 迭代反转前n个节点
        def reverseN (head, n):
            pre = None, cur = head
            while n!=0 :
                head = head.next
                n = n -1
            pre = head # pre需要指向successor

            while n!=0 :
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
                n = n-1
            
            return pre
        """

        
            