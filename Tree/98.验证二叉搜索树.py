# https://leetcode-cn.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ## 递归
        # 特点：中序遍历的结果是一个递增序列（这是充要条件吗？）
        order = []
        def traverse(root):
            if not root: return root
            traverse(root.left)
            order.append(root.val)
            traverse(root.right)
        traverse(root)
        for i in range(len(order)-1):
            if order[i]>=order[i+1]:
                return False
        return True

        ## 迭代
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right
        return True
        """