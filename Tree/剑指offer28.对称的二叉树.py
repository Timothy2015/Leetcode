# 递归解法


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        # 递归：根无需考虑，只需考虑两颗子树

        # 辅助函数
        def recur(L, R):
            if L==None and R==None: return True
            # if L==None and R!=None: return False
            # if L!=None and R==None: return False
            # if L.val != R.val: return False
            if not L or not R or L.val != R.val: return False

            # if L.left.val != R.right.val: return False
            # if L.right.val != R.left.val: return False
            # 同时满足，and与两者
            return recur(L.left, R.right) and recur(L.right, R.left)
        
        return recur(root.left, root.right)





"""一个失败的解法：权当练手"""

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        # 1-树的序列化--必须“中序遍历”
        strList = []
        def stringFy(root):
            if not root: 
                strList.append('#')
                return

            stringFy(root.left)
            strList.append(str(root.val))            
            stringFy(root.right)
        
        stringFy(root)        
        # while strList[len(strList)-1] == '#': strList.pop()
        strTree = "".join(strList)
        print(strTree)

        """竟然行不通:
        * 测试用例：[1,2,2,2,null,2] 或 [1,2,2,3,null,3]无法通过！
            * 此时，该树不对称，但是中序遍历是回文字符串!
        """

        # 2-回文字符串
        n = len(strTree)
        if n%2==0: return False
        cen = int((n-1)/2)
        left = cen - 1; right = cen + 1
        while left>=0 and right<=n-1 :
            if strTree[left] != strTree[right]:
                return False
            left -= 1
            right += 1
        return True
