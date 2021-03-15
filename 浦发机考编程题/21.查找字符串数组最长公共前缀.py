# 编写一个函数来查找字符串数组中的最长公共前缀， 若不存在公共前缀， 返回空字符串 “”

import sys

strs1 = ['aaa', 'abc', 'acd', 'aab']
strs2 = ['ab', 'abc', 'abeeedc', 'ab']

def longestComPrefix(strs):
    res = ''
    min_len = sys.maxsize
    # 获取最短字符串的长度
    for str in strs:
        if len(str) < min_len:
            min_len = len(str)

    # 外层for循环，公共前缀的最大长度
    # 内层for循环，依次比较每个字符串的第i个字符是否相同
    for i in range(min_len):
        for j in range(len(strs)-1):
            if strs[j][i] != strs[j+1][i]:
                return res
        res += strs[j][i]
    return res

print(longestComPrefix(strs1))
print(longestComPrefix(strs2))


