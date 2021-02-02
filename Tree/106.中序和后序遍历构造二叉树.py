# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        # 递归解法：后序遍历的最后一个值为根节点, 前序遍历作为辅助信息
        if inorder==None: return None

        def build(postStart, postEnd, inStart, inEnd):
            if inStart > inEnd: return None
        
            first = postorder[postEnd]
            idx = index[first]
            root = TreeNode(postorder[postEnd])

            leftSize = idx-inStart
            root.left = build(postStart, postStart+leftSize-1, inStart, idx-1)
            root.right = build(postStart+leftSize, postEnd-1, idx+1, inEnd)

            return root

        index = {ele:i for i,ele in enumerate(inorder)}
        return build(0, len(postorder)-1, 0, len(inorder)-1)