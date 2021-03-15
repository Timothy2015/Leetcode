# 输出字符串的最大回文子字符串的长度（输入一串字符串， 判断里面是否有回文字串， 如“12321”， 
# 有则输出其中最大的长度， 如“211232109” 输出 5）

# Leetcode-中等难度
# https://leetcode-cn.com/problems/longest-palindromic-substring/

""" 解题思路: 211232109
* 1. 回文串的判定：从中间外两边扩展，中间可以是单字符，也可以是（相同的）双字符
* 2. 穷举遍历的思路：
    * 每一个单字符判断一下回文串，记录最大长度
    * 每两个相邻的字符，判定一下回文串，记录最大长度
"""

def longestPalindSubstr(str):

    # 浦发机考python不能用切片
    def slice(str, i, j):
        res = ''
        # [i, j)
        for k in range(i, j):
            res += str[k]
        return res

    def palindSubstr(str, l, r):
        while l>=0 and r<=len(str)-1:
            if str[l] == str[r]:
                l -= 1
                r += 1
            else:
                break
        return slice(str, l+1, r)

    res = ''
    for k in range(len(str)-1):
        # 单字符遍历判定
        str1 = palindSubstr(str, k, k) 
        res = str1 if len(str1) > len(res) else res
        # 双字符串遍历判定
        str2 = palindSubstr(str, k, k+1) 
        res = str2 if len(str2) > len(res) else res

    return len(res)

str = '211232109'
print(longestPalindSubstr(str))



