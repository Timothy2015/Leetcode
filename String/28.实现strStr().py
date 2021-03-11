# https://leetcode-cn.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 字符串模式匹配
        # 两种方法：1.暴力匹配；2.KMP算法
        
        if len(needle)==0:
            return 0
        if len(haystack)==0:
            return -1
        
        # 获取next[]数组
        # next[i]表示子串中第i个字符的最长公共前缀（或称为最长公共子串）
        def getNext(str):
            next = [-1]*len(str) # next[0]=-1
            if len(str)>1:
                next[1] = 0
            i, j =1, 0
            while(i<len(str)-1):
                if str[i]==str[j]:
                    i += 1
                    j += 1
                    next[i] = j
                elif j==0:
                    i += 1
                    next[i] = j
                else:
                    j = next[j]
            return next
        
        # 字符串匹配过程
        next = getNext(needle)
        i = j = 0
        while(i<len(haystack) and j<len(needle)):
            if haystack[i]==needle[j]:
                i += 1
                j += 1
            elif j==0:
                i += 1
            else:
                j = next[j]
        if j==len(needle):
            return i-j
        else:
            return -1