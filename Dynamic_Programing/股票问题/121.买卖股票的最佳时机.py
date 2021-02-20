# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## 3-模板题解
        # transferFunc:
        #   dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        #   dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        #   一次完整的交易包括 buy 与 sell, 所以上面只在buy一处k-1就好
        #   第二行buy的操作，实质是把减法变成加法来处理（+(-prices[i])）

        # base case:
        #   dp[-1][k][0] = dp[i][0][0] = 0
        #   dp[-1][k][1] = dp[i][0][1] = -sys.maxsize (负的最小值，代表不可能，用负数原因在于求最大值，便于更新)
        """
        ## 此处k=1，代入查看结果
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i]) 
        dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-prices[i]) 
        # 列出一些确定的值
        dp[i-1][0][0] = 0
        # 可以发现：k不影响结果
        dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+prices[i]) 
        dp[i][1][1] = max(dp[i-1][1][1], -prices[i]) 
        # 简化后的状态转移方程
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], - prices[i])
        """
        
        # py3创建二维数组
        # dp = [[0 for i in range(len(prices))] for j in range(2)]  # 2 X N 矩阵
        dp = [[0 for j in range(2)] for i in range(len(prices))]  # N X 2 矩阵

        # base case
        # dp[-1][0] = 0
        # dp[-1][1] = -sys.maxsize
        ## 简化后的状态转移方程
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        # dp[i][1] = max(dp[i-1][1], - prices[i])

        dp_i_0 = 0; dp_i_1 = -sys.maxsize
        for i in range(len(prices)):
            """
            if i==0:
                # i=0时的初始条件
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            """
            # dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            # dp[i][1] = max(dp[i-1][1], - prices[i])
            dp_i_1 = max(dp_i_1, - prices[i])
        return dp_i_0

        ## 
        """
        新状态只和相邻的一个状态有关，其实不用整个 dp 数组，
        只需要两个变量（dp_i_0, dp_i_1）储存相邻的那个状态就足够了，这样可以把空间复杂度降到 O(1)
        因为，总是交替轮换，只会用到上一次的这两个值，可以共享内存
        """

        
        ## 2-一次遍历，低买高卖（操作多次） - 画出股票走势折线图，一目了然
        """
        maxProfit = 0
        minLocal = 10000
        for price in prices:
            # 模拟在当下卖出股票
            maxProfit = max(maxProfit, price-minLocal)
            # 其后再更新minLocal，即体现了“历史最低点”
            minLocal = min(minLocal, price)
        return maxProfit
        """

        # 下面的解法有误：寻找历史最低点（时间序），而不是全局最低点
        """
        minLocal = 10000
        maxLocal = -1
        maxProfit = 0
        for i in range(0, len(prices)):
            if prices[i] < minLocal:
                minLocal = prices[i]
            if prices[i] > maxLocal:
                maxLocal = prices[i]
        maxProfit = maxLocal - minLocal
        return maxProfit
        """

        ## 1-暴力解：双重for循环(超出时间限制)
        """
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if maxProfit < prices[j] - prices[i]:
                    # 不要轻易使用列表
                    # profit.append(prices[j] - prices[i]) 
                    maxProfit = prices[j] - prices[i]
        return maxProfit
        """