# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """递归解法"""
        if head == None: return head

        # 递归出口/base case
        if head.next == None:
            return head
        # 递归主体
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return last


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        """迭代解法"""
        # 空链表 或 单元素列表
        if head == None or head.next == None: return head

        # 双指针: 该解法来自在本子上自己运行通了一个例子，还可以再优化！
        p = head; q = head.next
        p.next = None 
        while True:
            temp = p
            p = q.next
            q.next = temp
            # 如果p指向了None,结束
            if p == None:
                return q
            
            temp = q
            q = p.next
            p.next = temp
            # 如果q指向了None,结束
            if q == None:
                return p
        
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        """迭代解法: 经典的cur,pre版本"""
        # 空链表 或 单元素列表
        if head == None or head.next == None: return head

        # 双指针 cur, pre
        pre = None
        cur = head
        while cur!=None:
            # 这个相当于我之前p,q版时p，q交替保存下一个节点，免得修改后找不到下家
            next = cur.next 
            cur.next = pre
            pre = cur 
            cur = next
        # cur最终指向None，上面的循环终止，所以返回pre
        return pre

