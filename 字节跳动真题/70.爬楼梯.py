# https://leetcode-cn.com/problems/climbing-stairs/

# 精选题解：https://leetcode-cn.com/problems/climbing-stairs/solution/hua-jie-suan-fa-70-pa-lou-ti-by-guanpengchn/

class Solution:
    def climbStairs(self, n: int) -> int:

        ## 四、动态规划，状态转移方程f(n) = f(n-1) + f(n-2)
        """
        dp = [0]*(n+1) 
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        """

        ## 只与前两个状态相关，只要两个变量即可，空间复杂度O(1)
        # * 缺点：多两行处理边界
        if n==1: return 1
        if n==2: return 2
        dp_n_1 = 1
        dp_n_2 = 2
        for i in range(3, n+1):
            dp_i = dp_n_1 + dp_n_2
            dp_n_1 = dp_n_2
            dp_n_2 = dp_i
        return dp_i

        ## 三、使用hash表来剪枝 + 递归 (依然超出时间限制)
        # mp = collections.defaultdict(int)

        ## 二、使用递归 (超出时间限制)
        """
        # * f(n) = f(n-1) + f(n-2)
        # base case 
        if n==1: return 1
        if n==2: return 2
        # 剪枝操作
        if n in mp:
            return mp[n]
        else:
            mp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return mp[n]
        # return self.climbStairs(n-1) + self.climbStairs(n-2)
        """

        ## 一、暴力枚举：a + 2b = n
        # * b <= n//2
        # * a = n-2b, 0<=a<=n