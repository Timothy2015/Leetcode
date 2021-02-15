class Solution:
    def waysToChange(self, n: int) -> int:
        # 推断类型：完全背包问题
        """背包问题描述：
        * 背包容量：n
        * 物体种类和价值：4，coins[25, 10, 5, 1]
        * 特点：每种物体的数量不限，完全背包问题    
        """
        coins = [25,10,5,1]
        N = 4; M = n;
        # dp数组
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        # base case: N为0,表示种类为0; M为0，表示种类为1，什么都不选（题目测试印证base case）
        for i in range(N+1):
            dp[i][0] = 1
        # 状态转移方程
        """dp[i][j]的含义：使用前i中硬币，组合为j的表示法的种类"""
        for i in range(1,N+1):
            for j in range(1,M+1):
                if j - coins[i-1] < 0:
                    dp[i][j] = dp[i-1][j] #题目要求什么，状态转移什么
                else:
                    # 求总数 = 不用第i种的情况数 + 用第i种的情况数
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
        # (结果可能会很大，你需要将结果模上1000000007)
        return dp[N][M]%1000000007

"""--------------状态压缩--------------"""
class Solution:
    def waysToChange(self, n: int) -> int:
        # 推断类型：完全背包问题
        """背包问题描述：
        * 背包容量：n
        * 物体种类和价值：4，coins[25, 10, 5, 1]
        * 特点：每种物体的数量不限，完全背包问题    
        """
        coins = [25,10,5,1]
        N = 4; M = n;
        # dp数组
        dp = [0 for i in range(M+1)]
        # base case: N为0,表示种类为0; M为0，表示种类为1，什么都不选（题目测试印证base case）
        dp[0] = 1
        # 状态转移方程
        """dp[j]的含义：使用前i中硬币，组合为j的表示法的种类"""
        for i in range(0,N):
            for j in range(1,M+1):
                if j - coins[i] >= 0:
                    dp[j] = dp[j] + dp[j-coins[i]]
        return dp[M]%1000000007


"""----------通过 显示详情 - 查看用时最短的提交代码 """
class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7

        ans = 0
        for i in range(n // 25 + 1):
            rest = n - i * 25
            a, b = rest // 10, rest % 10 // 5
            ans += (a + 1) * (a + b + 1)
        return ans % mod

class Solution:
    def waysToChange(self, n: int) -> int:
        self.ret=0
        for i in range(n//25+1):
            tempn=n-i*25
            temp5=tempn//5+1
            self.ret+=((temp5+1)%2+1+temp5)*((temp5+1)//2)//2
            
        return self.ret%1000000007
