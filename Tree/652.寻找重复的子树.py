# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # 递归求解
        # 一个节点要做什么：
        #   1.以自己为根的子树长什么样子（子问题：二叉树的序列化）
        #   2.以其他的节点为根的子树长什么样子，比较是否有重复节点

        # 辅助函数：子树序列化
        def traverse(root):
            if not root: return "#"

            left = traverse(root.left)
            right = traverse(root.right)
            # 左子树样子 + 右子树样子 + 我自己
            subTree = left + "," + right + "," + str(root.val)
            
            # 返回subTree之前的操作
            if memo[subTree]==1: # 第一次重复的时候计数
                res.append(root)
            
            # Counter添加元素的操作：加入当前的子树
            memo[subTree] += 1

            return subTree
        
        memo = collections.Counter()        
        res = []
        traverse(root)
        return res