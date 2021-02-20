# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        ## 默写模板
        """
        # transfer function
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # base case
        dp[0][k][0] = 0
        dp[0][k][1] = -prices[0]
        dp[i][0][0] = 0
        dp[i][0][1] = -sys.maxsize
        """
        # 分析差异：
        # 1.多了一笔手续费，既然k-1放在buy处，手续费也放在buy处（不行）
        #   * 手续费的支出，需要放在sell处，卖出一次交一次fee，卖出之后的结果才是想要的结果，保证没有漏交费
        # 2.k=infinity, k=k-1
        # 3.只能相邻的状态有关
        # dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
        # dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i] - fee)

        if not prices: return 0

        dp_i_0 = 0;
        dp_i_1 = -prices[0]
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i] - fee) # 卖出一次，交一次手续费
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i])
        return dp_i_0

