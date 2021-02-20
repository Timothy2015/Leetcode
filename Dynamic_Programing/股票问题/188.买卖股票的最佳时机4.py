# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
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
        if not prices: return 0
        m = k
        # N X k X 2
        dp = [[[0 for i in range(2)] for j in range(m+1)] for k in range(len(prices))]
        for i in range(len(prices)):
            for k in range(1, m+1): # k=1,...,m 只能遍历m次，所以不能从0开始
                if i==0:
                    # base case
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        return dp[len(prices)-1][m][0]

