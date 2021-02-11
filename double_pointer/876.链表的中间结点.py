# https://leetcode-cn.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        # 快慢双指针
        slow = head; fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 上述循环结束，slow的位置恰好就是题目要求的中点位置
        # 奇数：正中； 偶数：第二个中间节点
        return slow

"""
寻找链表中点的一个重要作用是对链表进行归并排序。
回想数组的归并排序：求中点索引递归地把数组二分，最后合并两个有序数组。对于链表，合并两个有序链表是很简单的，难点就在于二分。
但是现在你学会了找到链表的中点，就能实现链表的二分了。关于归并排序的具体内容本文就不具体展开了。
"""