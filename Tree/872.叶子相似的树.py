class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # 辅助函数：遍历叶子(生成字符串) -- 后序遍历
        def leaf(root, strLeaf):
            # 后序遍历
            if not root: return
            leaf(root.left, strLeaf)
            leaf(root.right, strLeaf)
            if not root.left and not root.right:
                strLeaf.append(str(root.val))
            # print(','.join(strLeaf))
            return ','.join(strLeaf)

        # leaf(root1,[])
        # leaf(root2,[])
        return leaf(root1, []) == leaf(root2, [])