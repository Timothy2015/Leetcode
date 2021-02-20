# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## 默写模板
        """
        # 转移方程：i-天数 k-交易次数 0/1-有无股票
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # base case
        dp[0][k][0] = 0
        dp[0][k][1] = -prices[0] # 买进
        dp[i][0][0] = 0
        dp[i][0][1] = -sys.maxsize
        """
        # 分析差异：多了一天的冷冻期 + 'k=infinity'即k=k-1
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-2][k][0] - prices[i]) # 延迟一天再买入

        if not prices: return 0

        dp_i_0 = 0; 
        dp_i_1 = -prices[0]
        # dp_i_1 = -sys.maxsize
        # 变量 dp_pre 代表 dp[i-2][0]
        dp_pre = 0
        for i in range(len(prices)):
            # 难点：dp_pre怎么更新?
            
            # 前一天卖出之后
            temp = dp_i_0 
            
            # 经过第i天的操作
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_pre - prices[i])

            # 更新dp_pre为前一天的卖出之后的dp_i_0
            dp_pre = temp
        return dp_i_0
