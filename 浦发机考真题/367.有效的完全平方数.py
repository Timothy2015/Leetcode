# https://leetcode-cn.com/problems/valid-perfect-square/submissions/

# 题解：https://zhuanlan.zhihu.com/p/33378294

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        ## 暴力求解，内存溢出
        # if num==1: 
            # return True
        # for i in range(int(num/2), 1, -1):
        #     if i*i == num:
        #         return True

        ## 二分查找: [left, right]]，闭合区间
        # * 期间导致时间超出限制，是因为while死循环
        """
        left = 1
        right = int(num/2)+1
        while left <= right:
            mid = left + int(right-left)/2
            if mid*mid == num:
                return True
            elif mid*mid < num:
                # print(left, right)
                left = mid + 1
            else:
                right = mid - 1
        return False
        """
    
        ## 数学方法1：n**2 = [n*(1 + 2*n-1)]/2
        # n**2 = 1 + 3 + 5 + 7 + 9 + ... + 2*n-1
        # 可以让num一直减奇数数列，看最后是否为0
        """
        if num < 0: return False
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0
        """

        ## 数学方法2：牛顿法，切线逼近的思想
        # x**2 = n 转换为 x**2 - n = 0
        x = num
        while x*x > num:
            # x = [x + num/x]/2，上面公式化解的结果
            x = int(x + num/x) >> 1 # 右移一位除以2
        return x * x == num