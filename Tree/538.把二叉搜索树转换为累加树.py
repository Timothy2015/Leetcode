# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        # 小树的原始解法：有待优化
        # * 思考1：能不能只遍历一次，边遍历边修改？
        # * 思考2：能不直接实现逆序的遍历？--可以，交换左右子树的遍历顺序
        nums = []
        def traverse(root, mode):
            if not root: return 
            traverse(root.left, mode)
            if mode==1:
                nums.append(root.val)
            if mode==2:
                root.val = nums[0]
                nums.pop(0)
            traverse(root.right, mode)
        traverse(root,1)
        # print(nums)
        for i in range(len(nums)-2,-1,-1):
            nums[i] += nums[i+1]
        # print(nums)        
        traverse(root,2)
        return root


"""优化后的解法：只遍历一次，边遍历边修改节点的值"""
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # 改进：只遍历一次，边遍历边修改节点的值
        # 关键：交换左右子树的顺序，实现逆序的遍历
        sum_ = 0
        def traverse(root):
            nonlocal sum_
            if not root: return
            traverse(root.right)
            sum_ += root.val
            root.val = sum_
            traverse(root.left)
        traverse(root)
        return root

