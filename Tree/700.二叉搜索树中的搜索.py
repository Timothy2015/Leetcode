# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 迭代求解 -- 辅助结构：栈（python的栈用list实现 / queue.LifoQueue）
        # list模拟栈：
        # * list.append() #末尾添加
        # * list.pop() #末尾弹出末尾元素
        
        while root and root.val!=val:
            root = root.left if root.val>val else root.right
        return root

