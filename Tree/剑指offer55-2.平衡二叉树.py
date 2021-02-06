# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 递归解法1：要求 -- 自底向上（后序遍历）
        # 辅助函数：树的深度
        """
        def height(root):
            if not root: return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            # if abs(leftHeight - rightHeight)>1:
            if abs(leftHeight - rightHeight)>1 or leftHeight==-1 or rightHeight==-1:
                return -1
            else: # 剪枝
                return max(leftHeight, rightHeight) + 1
        # print(height(root))
        # return height(root)>=0
        return height(root) != -1
        """

    # def isBalanced(self, root: TreeNode) -> bool:
        # def recur(root):
        #     if not root: return 0
        #     left = recur(root.left)
        #     if left == -1: return -1  # 剪枝1
        #     right = recur(root.right) 
        #     if right == -1: return -1 # 剪枝2
        #     return max(left, right) + 1 if abs(left - right) <= 1 else -1

        # return recur(root) != -1


        # 递归解法2：要求 -- 自顶向下（先序遍历）
        """思路容易想到，但是比较慢！"""
        def height(root):
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1
        
        if not root: return True
        # return abs(height(root.left) - height(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        if abs(height(root.left) - height(root.right))>1 
            return -1
        else: # 剪枝可以加速
            return self.isBalanced(root.left) and self.isBalanced(root.right)