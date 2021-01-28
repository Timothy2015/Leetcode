class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # 题目要求什么，状态转移什么
        """完全背包问题
        * 背包容量：amount
        * 物体种类与价值：len(coins), coins
        * 特点：每个物体的数量不限，属于完全背包问题，套路一样，转移方程有些许差异
        """
        N = len(coins); M = amount
        # dp数组
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        # base case: N为0，组合数为0；M为0，组合数为1，一个都不选（这点有题意确定）
        for i in range(N+1):
            dp[i][0] = 1
        # 状态转移方程
        """dp[i][j]的含义：使用i中面额的硬币凑成总金额为j的硬币组合数"""
        for i in range(1,N+1):
            for j in range(1,M+1):
                if j-coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    # 求组合数总数，两种情况相加：
                    # 1.不适用第i种硬币凑成金额 j 的组合数
                    # 2.使用前i种硬币，凑成金额 j-coisn[i-1] 的组合数
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        return dp[N][M]

"""-------------状态压缩---------------"""
# class Solution:
    # def change(self, amount: int, coins: List[int]) -> int:
        # 题目要求什么，状态转移什么
        """完全背包问题
        * 背包容量：amount
        * 物体种类与价值：len(coins), coins
        * 特点：每个物体的数量不限，属于完全背包问题，套路一样，转移方程有些许差异
        """
        N = len(coins); M = amount
        # dp数组
        dp = [0 for i in range(M+1)]
        # base case: N为0，组合数为0；M为0，组合数为1，一个都不选（这点有题意确定）
        dp[0] = 1
        # 状态转移方程
        """dp[j]的含义：使用i中面额的硬币凑成总金额为j的硬币组合数"""
        for i in range(0,N):
            for j in range(1,M+1):
                if j-coins[i] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[M]

