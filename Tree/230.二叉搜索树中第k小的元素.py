# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ## 解法一：中序递归 + rank提前结束
        # BST的中序遍历为递增序列
        rank = 0
        res = 0
        def traverse(root, k):
            nonlocal rank,res
            if not root: return
            traverse(root.left, k)
            # 中序遍历位置
            rank += 1
            # print(rank)
            if rank==k:
                res = root.val
                """
                直接return root.val, 无法正确获得该结果
                递归找到会提前终止，需要另外定义变量保存结果
                """
                # return root.val
                return
            traverse(root.right, k)
        
        traverse(root, k)
        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ## 解法二：分治法
        # 辅助函数：统计节点
        def nodeCount(root):
            if not root: return 0
            # 后序遍历
            return nodeCount(root.left) + nodeCount(root.right) + 1
        
        leftN = nodeCount(root.left)
        if leftN+1 == k:
            return root.val
        elif leftN+1 < k:
            # self.kthSmallest(root.right, k-leftN-1)
            return self.kthSmallest(root.right, k-leftN-1)
        else:
            # self.kthSmallest(root.left, k)
            return self.kthSmallest(root.left, k)
