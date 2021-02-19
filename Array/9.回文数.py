# https://leetcode-cn.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        ### 最佳改进：只反转一半的数字
        # 前提：必须去掉特殊情况
        if x<0 or (x%10==0 and x!=0):
            return False
        # * 为了避免溢出，只反转一半: while(x > revertedNum)
        revertedNum = 0
        while (x > revertedNum) :
            revertedNum = revertedNum * 10 + x % 10 
            x //= 10 
        return x == revertedNum or x == revertedNum // 10
        # 当数字长度为奇数时，我们可以通过 revertedNum/10 去除处于中位的数字
        # 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNum = 123，
        # 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        
        """

        ## 思路一：转化为字符串，回文字符串的判定
        ## 思路二：数字就利用数字的特点来快速求解
        # * 反转数字，判断是否相同
        if x < 0: return False
        def reverse(num):
            res = 0
            while num:
                res = 10*res + num%10
                num = num // 10
            return res

        if x==reverse(x):
            return True
        else:
            return False
        """