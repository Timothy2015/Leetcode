"""
一共3种有效解法：
1. 先序遍历
2. 后序遍历：
    序列化，左-右-根
    还原时，根--右子树--左子树
3. 层次遍历：
    序列化：层次遍历，辅助队列
    还原时：层次遍历，辅助队列--队列存储父节点
注：中序遍历无效。
"""

"""先序遍历"""
iclass Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # str1 = '1' # id(str1)查看，str2和str1不是同一个内存地址
        strList = []
        # 先序遍历
        def stringFy(root):
            if not root: 
                strList.append('#')
                return
            
            strList.append(str(root.val))

            stringFy(root.left)
            stringFy(root.right)
        
        stringFy(root)
        # print(",".join(strList))
        return ",".join(strList)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        strList = data.split(',')
        print(strList)

        def parseStr(strList):
            if not strList: return None

            first = strList.pop(0) # 必须执行
            if first == '#':
                return None
            root = TreeNode(int(first))
            
            root.left = parseStr(strList)
            root.right = parseStr(strList)
           
            return root
       
        return parseStr(strList)



"""后序遍历"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # str1 = '1' # id(str1)查看，str2和str1不是同一个内存地址
        strList = []
        # 后序遍历
        def stringFy(root):
            if root==None: 
                strList.append('#')
                return

            stringFy(root.left)
            stringFy(root.right)
            # 后序遍历的位置
            strList.append(str(root.val))
        
        stringFy(root)
        # print(','.join(strList))
        return ','.join(strList)          

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        strList = data.split(',')
        print(strList)

        def parseStr(strList):
            if not strList: return None

            last = strList.pop(len(strList)-1) # 必须执行
            if last == '#':
                return None
            root = TreeNode(int(last))       
            
            """为什么要先构造右子树？因为strList中先遇到右子树"""
            root.right = parseStr(strList) 
            root.left = parseStr(strList)
            # root.right = parseStr(strList) 
           
            return root
    
        return parseStr(strList)

"""层次遍历"""
# python3

import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root: return '#'
        # 层次遍历（非迭代方式--辅助队列）
        q = collections.deque()
        q.append(root)
        strList = []

        while q:
            first = q.popleft()
            if first=='#': 
                strList.append('#')
                continue
            
            strList.append(str(first.val))
            
            if first.left: q.append(first.left)
            else: q.append('#')
            if first.right: q.append(first.right)
            else: q.append('#')

        # print(','.join(strList))
        return ','.join(strList)          

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        strList = data.split(',')
        print(strList)
        q = collections.deque()

        first = strList[0] # 必须执行
        if first == '#':
            return None
        root = TreeNode(int(first))  
        q.append(root)

        i = 1
        while i < len(strList) :
            parent = q.popleft()
            left = strList[i]; i+=1
            if left != '#':
                parent.left = TreeNode(int(left))
                q.append(parent.left)
            else:
                parent.left = None
            
            right = strList[i]; i+=1
            if right != '#':
                parent.right = TreeNode(int(right))
                q.append(parent.right)
            else:
                parent.right = None    
        
        return root

# java
"""
public class Codec {
    String SEP = ",";
    String NULL = "#";
    String serialize(TreeNode root) {
        if (root == null) return "";
    StringBuilder sb = new StringBuilder();
    // 初始化队列，将 root 加入队列
    Queue<TreeNode> q = new LinkedList<>();
    q.offer(root);

    while (!q.isEmpty()) {
        TreeNode cur = q.poll();

        /* 层级遍历代码位置 */
        if (cur == null) {
            sb.append(NULL).append(SEP);
            continue;
        }
        sb.append(cur.val).append(SEP);
        /*****************/

        q.offer(cur.left);
        q.offer(cur.right);
    }

    return sb.toString();
}

  
    public TreeNode deserialize(String data) {
        if (data.isEmpty()) return null;
        String[] nodes = data.split(SEP);
        // 第一个元素就是 root 的值
        TreeNode root = new TreeNode(Integer.parseInt(nodes[0]));

        // 队列 q 记录父节点，将 root 加入队列
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);

        for (int i = 1; i < nodes.length; ) {
            System.out.print(i);
            // 队列中存的都是父节点
            TreeNode parent = q.poll();
            // 父节点对应的左侧子节点的值
            String left = nodes[i++];
            if (!left.equals(NULL)) {
                parent.left = new TreeNode(Integer.parseInt(left));
                q.offer(parent.left);
            } else {
                parent.left = null;
            }
            // 父节点对应的右侧子节点的值
            String right = nodes[i++];
            if (!right.equals(NULL)) {
                parent.right = new TreeNode(Integer.parseInt(right));
                q.offer(parent.right);
            } else {
                parent.right = null;
            }
        }
        return root;
    }}
"""