# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

TODO
# 后序的改进点：（代码有点冗余）stringFy和stringFy2两个函数合并为一个函数。
# * 想到了：传入一个flag

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 树的序列化 -- 后序遍历
        # * 该题的思路与重复子树的问题非常相似
        def stringFy(root, strTree, flag):
            if not root: return '#'
            left = stringFy(root.left, strTree, flag)
            right = stringFy(root.right, strTree, flag)
            
            strTree = left + '-' + right + '-' + str(root.val)
            if flag: sStr.append(strTree)
            return strTree
        
        sStr = []
        sStr.append(stringFy(s, '', 1))
        tStr = (stringFy(t, '', 0))

        # print(sStr)
        # print(tStr)
        return tStr in sStr


# 冗余代码

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 树的序列化 -- 后序遍历
        # * 该题的思路与重复子树的问题非常相似
        def stringFy(root, strTree):
            if not root: return '#'
            left = stringFy(root.left, strTree)
            right = stringFy(root.right, strTree)
            
            strTree = left + '-' + right + '-' + str(root.val)
            sStr.append(strTree)
            return strTree
        
        sStr = []
        sStr.append(stringFy(s, ''))
        
        def stringFy2(root, strTree):
            if not root: return '#'
            left = stringFy(root.left, strTree)
            right = stringFy(root.right, strTree)
            
            strTree = left + '-' + right + '-' + str(root.val)
            return strTree

        tStr = (stringFy2(t, ''))

        # print(sStr)
        # print(tStr)
        return tStr in sStr