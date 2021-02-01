"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # if root.left == None and root.right == None: 
        #    return root
        # root.left.next = root.right
        
        # self.connect(root.left)
        # self.connect(root.right)

        # return root


        """上面的代码有缺陷：5和6节点无法connect起来，涉及到两个不同的父节点；
        * 解决思路（1）：创建一个辅助函数，增加参数
        """
        # 在这里面递归
        # def connectTwo(node1, node2):
        #     if node1==None and node2==None:
        #         return
        #     node1.next = node2

        #     connectTwo(node1.left, node1.right)
        #     connectTwo(node1.right, node2.left)
        #     connectTwo(node2.left, node2.right)

        # if root == None: return None
        # connectTwo(root.left, root.right)
        # return root


        """上面的代码有缺陷：5和6节点无法connect起来，涉及到两个不同的父节点；
        * 解题思路（2）：利用上已有node.next信息，在最初的不完整版上略加修改
        """
        if root==None: return None

        if root.left == None and root.right == None: 
           return root
        root.left.next = root.right
        # 利用已有node.next信息，串联起来两个节点
        root.right.next = root.next.left if root.next != None else None
        
        self.connect(root.left)
        self.connect(root.right)

        return root

        
        # 迭代版本
        """提交记录--用时最短的版本"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        first = root
        # 双层while循环
        while first.left:
            node = first
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next # 充分利用已有的node.next信息
            first = first.left
        return root


        """ 另一个思路：直观看过去，就是层次遍历
        * 解题思路（3）：队列--实现“层次遍历” 
        * 时间复杂度 O(N)
        * 空间复杂度 O(N) -- 这里不符合进阶的要求
        """
import collections 

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])
        
        # 外层的 while 循环迭代的是层数
        while Q:
            
            # 记录当前队列大小
            size = len(Q)
            
            # 遍历这一层的所有节点
            for i in range(size):                
                # 从队首取出元素
                node = Q.popleft()
                
                # 连接
                if i < size - 1:
                    node.next = Q[0]

                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        # 返回根节点
        return root

