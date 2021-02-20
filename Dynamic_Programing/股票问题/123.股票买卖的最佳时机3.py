# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
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
        # * k=2，方程不能简化，直接穷举就好
        # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        # dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
        # dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
        # dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])

        # 将i=0代入上面的方程
        """
        dp_i_10 = 0; dp_i_11 = - prices[0]
        dp_i_20 = 0; dp_i_21 = - prices[0]
        for i in range(len(prices)):
            # dp_i_11 = max(dp_i_11, dp_i_00 - prices[i]) # dp_i_00 = 0

            dp_i_10 = max(dp_i_10, dp_i_11 + prices[i])
            dp_i_11 = max(dp_i_11, - prices[i]) 
            dp_i_20 = max(dp_i_20, dp_i_21 + prices[i])
            print(dp_i_20)
            dp_i_21 = max(dp_i_21, dp_i_10 - prices[i])
        return dp_i_20
        """

        # """
        # NX2X2
        dp = [[[0 for i in range(2)] for j in range(3)] for k in range(len(prices))]
        # transfer function
        # dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1] + prices[i])
        # dp[i][1][1] = max(dp[i-1][1][1], - prices[i])
        # dp[i][2][0] = max(dp[i-1][2][0], dp[i-1][2][1] + prices[i])
        # dp[i][2][1] = max(dp[i-1][2][1], dp[i-1][1][0] - prices[i])

        for i in range(len(prices)):
            # base case
            if i==0:
                # i-天数 k-交易次数 0/1-有无股票
                dp[i][0][0] = 0
                dp[i][0][1] = - prices[i]
                dp[i][1][0] = 0
                dp[i][1][1] = - prices[i]
                dp[i][2][0] = 0
                dp[i][2][1] = - prices[i]
                continue
            for k in range(1, 3): # k=1,2 只能遍历两次
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[len(prices)-1][2][0]        
        # """