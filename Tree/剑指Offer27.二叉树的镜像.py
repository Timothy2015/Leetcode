# https://leetcode-cn.com/problems/er-cha-shu-de-jing-xiang-lcof/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 注意一点：不是交换val，而是交换node
        if not root: return

        # temp_node = root.left
        # root.left = root.right
        # root.right = temp_node
        root.left, root.right = root.right, root.left

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)
        return root