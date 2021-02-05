
# 中序遍历 + 构造一棵新树
# * 时间复杂度：O(N)
# * 空间复杂度：O(N)
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # 递归：中序遍历
        res = []
        def cVisit(root):
            if not root: return NoneNN
            cVisit(root.left)
            res.append(root.val)
            cVisit(root.right)
        cVisit(root)
        # print(res)
        
        # 创建递增树
        root = TreeNode(None) #空节点
        ans = root
        while res:
            root.left = None
            root.right = TreeNode(res[0])
            root = root.right
            res.pop(0)
        return ans.right

# 在原树上修改：
# * 时间复杂度：O(N)
# * 空间复杂度：O(H)
class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
