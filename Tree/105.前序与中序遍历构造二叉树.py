"""改造成“闭包”，大大简化函数参数"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归解法：前序遍历的第一个值为根节点, 前序遍历作为辅助信息
        if preorder==None: return None

        def build(preStart, preEnd, inStart, inEnd):
            if inStart > inEnd: return None
        
            first = preorder[preStart]
            idx = index[first]
            root = TreeNode(preorder[preStart])

            leftSize = idx-inStart
            root.left = build(preStart+1, preStart+leftSize, inStart, idx-1)
            root.right = build(preStart+leftSize+1, preEnd, idx+1, inEnd)

            return root

        index = {ele:i for i,ele in enumerate(inorder)}
        return build(0, len(preorder)-1, 0, len(inorder)-1)

    # def build(self, preNums, n, inNums, lo, hi): 
    """preorder和inorder序列一样重要"""
    
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # 递归解法：前序遍历的第一个值为根节点, 前序遍历作为辅助信息
        if preorder==None: return None
        index = {ele:i for i,ele in enumerate(inorder)}
        return self.build(index, preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    # def build(self, preNums, n, inNums, lo, hi): 
    #preorder和inorder序列一样重要
    def build(self, index, preNums, preStart, preEnd, inNums, inStart, inEnd):
        if inStart > inEnd: return None

        # # 查找根节点在中序遍历中的位置
        # def find(first, inorder):
        #     idx = -1
        #     for i in range(len(inNums)):
        #         if inorder[i] == first:
        #             idx = i
        #             # 没有重复元素，找到即可return
        #             return idx
    
        first = preNums[preStart]
        idx = index[first]
        root = TreeNode(preNums[preStart])

        leftSize = idx-inStart

        root.left = self.build(index, preNums, preStart+1, preStart+leftSize, inNums, inStart, idx-1)
        root.right = self.build(index, preNums,preStart+leftSize+1, preEnd, inNums, idx+1, inEnd)

        return root
"""

        # 最快的提交方案：递归 + 字典提高查找效率
"""
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(pre_left, pre_right, in_left, in_right):
            # 终止条件
            if pre_left > pre_right:
                return None
            # 前序根下标
            pre_root = preorder[pre_left]
            # 中序根下标
            in_root = index[pre_root]

            root = TreeNode(pre_root)

            len_left = in_root - in_left

            root.left = myBuildTree(pre_left + 1, pre_left + len_left, in_left, in_root - 1)
            root.right = myBuildTree(pre_left + len_left + 1, pre_right, in_root + 1, in_right)
            return root

        n = len(preorder)
        index = {ele: i for i, ele in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)
    """

