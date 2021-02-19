# https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order/
# 精彩题解：https://leetcode-solution-leetcode-pp.gitbook.io/leetcode-solution/selected/byte-dance-algo-ex-2017#3-zi-dian-xu

class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        ## 2-十叉树的遍历 + 数字特点
        # 数字的特点：
        # 1. cur + 1, 进入下一颗树(总共1-9棵树)
        # 2. cur * 10, 进入树的下一层
        def count(Cur, Next, n):
            steps = 0
            # 注意这里的边界<=
            while Cur <= n: 
                # min()用来处理最后一层的边界问题（类似完全二叉树的节点统计）
                # n+1的原因是n从1开始，而不是0
                steps += min(n+1, Next) - Cur
                Cur *= 10
                Next *= 10
            return steps
        
        cur = 1
        # 遍历x个点，k减去x，直到K=0,返回cur
        k = k - 1
        while k>0:
            steps = count(cur, cur+1, n)
            if steps <= k:
                # 去到下一棵树
                cur += 1
                k -= steps
            else:
                # 进入下一层
                cur *= 10
                k -= 1
        return cur     

        ## 1-2 暴力 + 堆结构
        ## 1-1 暴力解垫底（超出时间限制）
        """
        nums = [str(i) for i in range(1, n+1)]
        return sorted(nums)[k-1]
        """