# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    """
    def levelOrder(self, root: TreeNode) -> List[List[int]]:        
        if root==None: return []
        # 层次遍历 --> 层序遍历（需要考虑深度！）
        # 迭代解法：
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q) # 当前列表长度，正好为，当前层的节点个数
            temp = []
            for _ in range(size):
                if q[0].left!=None: q.append(q[0].left)
                if q[0].right!=None: q.append(q[0].right)
                temp.append(q[0].val)
                q.popleft()
            res.append(temp)
        # print(res)
        return res
        """
        
        # 递归解法（速度竟然最快！）
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        level = 0
        self.level(root, 0, res)
        return res

    def level(self, root, level, res):
        if not root: return []
        """先序遍历的位置 | 思考：当前节点应该做些什么？"""
        # 一开始：len(res)=len([])=0,level=0
        if len(res) == level: res.append([]) # 创建一个[]保存当前层的val
        res[level].append(root.val)

        if root.left: self.level(root.left, level+1, res)
        if root.right: self.level(root.right, level+1, res)

        """队列：遍历完上一层，留在队列里的恰好是下一层的所有节点"""
        ### 下面的处理好复杂，对不对，以后这种情况不要继续做下去了，……
        ### 静下来想一想：有什么重要的“隐含条件”没有用上？

        # result = []; temp = []; n = 1
        # for i in range(len(res)):
        #     if res[i] != "#":
        #         temp.append(res[i])
        #     m = i+1

        #     if (m+1)%(2**n) == 0:
        #         result.append(temp)
        #         temp = []
        #         n = n + 1
        # if temp!=[]:
        #         result.append(temp)