class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #---子集背包问题---
        # 求数组的和，转化为背包问题
        sum = 0
        for num in nums:
            sum += num
        # 如果sum不为偶数，则返回False
        if sum % 2 != 0 : return False

        # 定义二维数组, 多创建一行和一列
        N = len(nums) ; M = int(sum/2)
        # dp = [[False for i in range(N+1) ] for j in range(M+1)] # M+1列，N+1行
        dp = [[False for i in range(M+1) ] for j in range(N+1)] # N+1行，M+1列
        # base case
        # dp[:][0] = True # 不i用装就满了--【切片赋值失效】
        for t in range(N+1) :
            dp[t][0] = True
        # 核心代码
        for i in range(1,N+1):
            for w in range(1,M+1):
                if w - nums[i-1] < 0 :
                    # 背包容量不足，不能装进第i个物体
                    dp[i][w] = dp[i-1][w]
                else:
                    # 关键在这里：理解状态之间的转移
                    #!-如果dp[i-1][w-nums[i-1]为True,则加入nums[i-1],恰好也为true,即刚好装满-!
                    # 这里还是需要把不装的情况考虑进来，不装已经满了，则不装
                    dp[i][w] = dp[i-1][w] or dp[i-1][w-nums[i-1]]
        return dp[N][M]

### ----------------------- 状态压缩 -----------------------
""" 仔细观察：第24和29行的操作：
    * i 每进行一轮迭代，dp[w]其实就相当于dp[i-1][w].所以只需要一维数组就够用了
    * 唯一需要注意的是 j 应该从后往前反向遍历，因为每个物品（或者说数字）只能用一次，
      以免之前的结果影响其他的结果。
 """
class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        #---子集背包问题---
        # 求数组的和，转化为背包问题
        sum = 0
        for num in nums:
            sum += num
        # 如果sum不为偶数，则返回False
        if sum % 2 != 0 : return False;

        # 定义二维数组, 多创建一行和一列
        N = len(nums) ; M = int(sum/2)
        dp = [False for i in range(M+1)]
        # base case
        dp[0] = True
        # 核心代码
        for i in range(1,N+1):
            for w in range(M, 0, -1): # 倒着遍历，range()用法需要熟练
                # print(w)
                if w - nums[i-1] >= 0 :
                    dp[w] = dp[w] or dp[w - nums[i-1]]
        return dp[M]
