# https://leetcode-cn.com/problems/count-complete-tree-nodes/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 获取(普通)树的高度
        """
        def getDepth(root):
            if not root: return 0
            return 1 + max(getDepth(root.left), getDepth(root.right))
        """
        # 获取完全二叉树的高度（左右子树也是完全二叉树）
        def getDepth(root):
            if not root: return 0
            # 完全二叉树：左子树的高度代表树的高度
            return 1 + getDepth(root.left)

        # 如果左右子树高度相同：左边为满二叉树，右边为完全二叉树
        # 如果左右子树高度不同：左边为完全二叉树，右边为满二叉树
        if not root: return 0

        LD = getDepth(root.left)
        RD = getDepth(root.right)
        if LD == RD:
            # 根 + 左子树节点数 + 右子树节点数
            return 1 + (2**LD-1) + self.countNodes(root.right)
        else:
            return 1 + (2**RD-1) + self.countNodes(root.left)
        
        
