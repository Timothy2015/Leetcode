# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        root = self.build(nums, 0, len(nums)-1)
        return root

    # 独立的构造一个辅助函数（后面优化再改造成“闭包”）
    # max（build）一个参数不够，三个参数最好：
    def build(self, nums, lo, hi):
        if lo > hi: return None

        maxVal = -1; idx = -1
        for i in range(lo, hi+1):
            if nums[i]>maxVal:
                maxVal = nums[i]
                idx = i
        # return max, idx
        root = TreeNode(maxVal)
        # print(root)
    
        # root.left = self.build(nums, 0, idx-1)
        # root.right = self.build(nums, idx+1, len(nums)-1)
        ### 为什么会有死循环？--下标范围出错
        root.left = self.build(nums, lo, idx-1)
        root.right = self.build(nums, idx+1, hi)

        return root