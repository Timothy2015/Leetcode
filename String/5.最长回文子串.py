# https://leetcode-cn.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 思路：先找到每一个回文子串，再比较每个子串长度，返回最长回文子串
        # 双指针：从中心开始，向两边扩展，寻找回文子串
        def palindrome(s, i, j):
            # while s[i]==s[j] and i>=0 and j<=len(s)-1: #测试用例："a"
            while i>=0 and j<=len(s)-1 and s[i]==s[j]:
                i -= 1
                j += 1
            return s[i+1:j]
        res = ''
        for k in range(len(s)):
            # 2021.2.8 我的错解，把问题搞复杂了，理解有误 #测试用例："abb
            # * 这里要做的分类是：
            # 1. 以s[k]为中心的子串 —— 作为奇数串
            #      - a / b / b 为中心
            # 2. 以s[k]和s[k+1]为中心的子串 —— 作为偶数串
            #      - ab / bb 为中心（地毯式搜索，全面覆盖）
            """
            # 奇数
            if (k+1)%2==1:
                i = int(k/2)
                str1 = palindrome(s,i,i)
                res = str1 if len(res) < len(str1) else res
            # 偶数
            if (k+1)%2==0:
                i = int((k-1)/2)
                j = i + 1
                str2 = palindrome(s,i,j)
                res = str2 if len(res) < len(str2) else res
            """
            str1 = palindrome(s,k,k)
            res = str1 if len(res) < len(str1) else res
            str2 = palindrome(s,k,k+1)
            res = str2 if len(res) < len(str2) else res
        return res


