# https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/

class Solution(object):
    def reverseLeftWords(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        ## python3强大的切片操作
        # s = list(s)
        # for i in range(n):
        #     s.append(s[i])
        # return ''.join(s[n:])

        ## 最快的方法：直接切s片再拼接
        # s1 = s[:n]
        # s2 = s[n:]
        # return s2+s1

        # or
        ss = s + s
        return ss[n:len(s)+n]
