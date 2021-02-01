# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """            
        # 关键的逻辑：
        # 1.先把左、右子树拉平
        # 2.再把左子树的右侧链表按序接到右子树的右侧链表，左子树置空
        if root == None: return
        # 拉平左、右子树，相信它
        self.flatten(root.left)
        self.flatten(root.right)

        # 拼接
        L = root.left
        R = root.right

        root.left = None
        root.right = L 

        temp = root # root.left为None, L也为None
        while temp.right != None:
            temp = temp.right
        temp.right = R

        """迭代版本"""
    # def flatten(self, root: TreeNode) -> None:
    #     curr = root
    #     while curr:
    #         if curr.left:
    #             predecessor = nxt = curr.left
    #             while predecessor.right:
    #                 predecessor = predecessor.right
    #             predecessor.right = curr.right
    #             curr.left = None
    #             curr.right = nxt
    #         curr = curr.right
