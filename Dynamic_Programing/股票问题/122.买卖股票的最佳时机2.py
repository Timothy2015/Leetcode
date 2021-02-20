# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/ 

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## 默写模板
        """
        # transfer function: i-天数 k-交易次数 0/1-是否持有股票
        # 注意：只有一个[k-1]，因为一次交易包括buy和sell完整过程，减一次就好
        dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k-1][1] + prices[i])
        dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k][0] - prices[i])
        # base case 
        dp[-1][k][0] = 0  #i从0开始，i=-1表示没开始，可以给出确定值
        dp[-1][k][1] = -sys.maxsize
        ## 优化，其实这里i可以从0
        dp[0][k][0] = 0 # 没做交易，也无法卖，利润为0
        dp[0][k][1] = -prices[i]  # 做了交易，只能买进

        dp[i][0][0] = 0
        dp[i][0][1] = -sys.maxsize #没有交易不可能有股票
        """
        # k = +inifinity （k为正无穷）
        ## 关键理解：k == k-1 (直接去掉k)
        """
        dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        # 只跟相邻的上一次有关，两个变量即可

        # base case
        dp[0][0] = 0
        dp[0][1] = -prices[i]
        """
        dp_i_0 = 0; dp_i_1 = -prices[0]
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, dp_i_0 - prices[i]) # 一旦没有了股票，立即买入
        return dp_i_0

        ## 留下一个问题：利用模板，自己做对了都不知道为什么？怎么解释自己的代码呢
        # 参考官方题解来理解
        ## 贪心策略：非常好理解, 所有的价差都收集起来，就是最大利润！
        """
        public:
            int maxProfit(vector<int>& prices) {   
                int ans = 0;
                int n = prices.size();
                for (int i = 1; i < n; ++i) {
                    ans += max(0, prices[i] - prices[i - 1]);
                }
                return ans;
            }
        };
        """
