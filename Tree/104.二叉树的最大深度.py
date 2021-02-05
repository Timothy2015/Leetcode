# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""深度优先搜索：
    * 1.后序遍历
    * 2.先序遍历
    * 3.中序遍历
"""

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def height(root) -> int:
            # 后序遍历（比先序遍历更优）
            if not root: return 0
            leftHight = height(root.left)
            rightHight = height(root.right)

            return max(leftHight, rightHight) + 1
        return height(root)
# 再简化：最简洁的代码
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
    

"""广度优先搜索：
    * 层次遍历
"""
# java
"""
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        int ans = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size > 0) {
                TreeNode node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
                size--;
            }
            ans++;
        }
        return ans;
    }
}
"""