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
    def isPalindrome(self, head: ListNode) -> bool:
        # 边界
        if head==None or head.next == None: return True

        # 如何优化空间复杂度：O(1),即需要再原链表上反转（比较完之后可以还原）
        ## 类比字符串判断回文串从中间开始
        # 快慢双指针：slow，fast -- 定位到链表的中间位置（实际为中间位置的后一个位置，因中间无需比较）
        slow = head; fast = head
        while (fast!=None and fast.next!=None) :
            slow = slow.next
            fast = fast.next.next
        if fast!=None:
            slow = slow.next # 奇数链表，slow还要再往前一步

        # 递归反转
        def reverse(head):
            if head.next == None:
                return head
            last = reverse(head.next)
            head.next.next = head
            head.next = None
            return last
        slow = reverse(slow)
        
        while slow!=None:
            if slow.val != head.val: 
                return False
            head = head.next
            slow = slow.next
        
        return True

"""增加难度：添加了“还原链表的要求，思路参考labuladong的相关题解”"""
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 边界
        if head==None or head.next == None: return True

        # 如何优化空间复杂度：O(1),即需要再原链表上反转（比较完之后可以还原）
        ## 类比字符串判断回文串从中间开始
        # 快慢双指针：slow，fast -- 定位到链表的中间位置（实际为中间位置的后一个位置，因中间无需比较）
        slow = head; fast = head
        while (fast!=None and fast.next!=None) :
            ## 还原指针
            backP = slow

            slow = slow.next
            fast = fast.next.next
        if fast!=None:
            ## 还原指针
            backP = slow 
            slow = slow.next # 奇数链表，slow还要再往前一步

        # 递归反转
        def reverse(head):
            if head.next == None:
                return head
            last = reverse(head.next)
            head.next.next = head
            head.next = None
            return last
        slow = reverse(slow)
        ## 还原指针
        backQ = slow
        headT = head
        
        while slow!=None:
            if slow.val != head.val: 
                ## 还原链表
                backP.next = reverse(backQ)
                # print(headT.next.next.next.next.val)

                return False
            head = head.next
            slow = slow.next
        

        ## 还原链表
        backP.next = reverse(backQ)
        # print(headT)

        return True






class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 边界
        if head==None or head.next == None: return True

        # 最简单的方法：先反转生成一个新链表，比较两个链表是否相同
        """思路简单，但是又笨又不好写(不好写的地方是复制了一份链表)，只是练练手"""
        # 复制一份链表
        newHead = ListNode(head.val)
        p = newHead
        q = head
        while q.next!=None:
            p.next = ListNode(q.next.val)
            p = p.next
            q = q.next
        
        # 递归反转
        def reverse(head):
            if head.next == None:
                return head
            last = reverse(head.next)
            head.next.next = head
            head.next = None
            return last
        newHead = reverse(newHead)

        while head!=None:
            if head.val != newHead.val:                
                return False
            head = head.next
            newHead = newHead.next
        return True
