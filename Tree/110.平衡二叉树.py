# 参考leetcode官方题解

"""解法一：递归 --- 自顶向下
    * 比较简单直接
    * 缺点：时间复杂度高 - 因为height()被重复调用了，需要剪枝；但更好的方法是采用后序遍历（自底向上的递归）。
"""

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True

        # 获取树的高度
        """还有一个改进点：去掉参数h，直接用数字，结果返回数字""""
        def height(root, h):
            if not root: return h
            else: h += 1
            return max(height(root.left, h), height(root.right, h))

        # 每个节点的左右两个子树的高度差的绝对值不超过1
        if abs(height(root.left, 0) - height(root.right, 0)) > 1:
            return False
        else: # 剪枝，提前结束递归
        # self.isBalanced(root.left) 
        # self.isBalanced(root.right)
        # return True
            return self.isBalanced(root.left) and self.isBalanced(root.right)

"""解法二：递归 --- 自底向上
    * 稍微复杂些，不太好想
    * 同样的，也用到了剪枝，剪枝条件：一有子树不平衡，整棵树就不平衡，提前结束递归。
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 获取树的高度
        def height(root) -> int:
            # 后序遍历
            if not root: return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)

            if abs(leftHeight - rightHeight)>1: # 这句话不够，忽略了子树不平衡的问题
            # if abs(leftHeight - rightHeight)>1 or leftHeight==-1 or rightHeight==-1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1  #1是根

        # print(height(root))
        return height(root)>=0



