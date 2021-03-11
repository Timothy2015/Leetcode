# 给定一个字符串，一个子串，判断子串在该字符串中出现的次数
## 理解题意：
# * A: abbbc
# * B: bb
# 上面的示例情况，bb出现算一次，还是两次？（按两次的情况做题，应该算两次）

txt = "ccccccccbccccb"
pat = "cccc"

# solution1: force
"""
def countPat(txt, pat):
    # txt代表母串，pat代表子串（模式串）
    cnt = 0
    m = len(txt)
    n = len(pat)
    # txt的前m-n+1个字符都需要尝试匹配一次
    for i in range(m-n+1):
        j = 0
        while i < m and j < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            else:
                break
        # 完整匹配后，j=n结束上面的while循环
        # if j == n-1:
        if j == n:
            cnt += 1
    return cnt

print(countPat(txt, pat))
"""

# solution2: KMP

# 参考：https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/qi-ta-suan-fa-wen-ti/dong-tai-gui-hua-zhi-kmp-zi-fu-pi-pei-suan-fa#yi-kmp-suan-fa-gai-shu
# labuladong-使用二维next数组


# 使用一维next数组
def strStr(haystack, needle):
    # 字符串模式匹配 -- KMP算法 (关键：如何获取next数组)

    cnt = 0
    m = len(haystack)
    n = len(needle)
    
    if n == 0:
        # pat为空时返回0
        return 0
    if m == 0:
        return 0
    
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
    while i < m-n+1:
        j = 0
        while i < m and j < n :
            if haystack[i]==needle[j]:
                i += 1
                j += 1
            elif j==0:
                i += 1
            else:
                j = next[j]
        if j == n:
            i = i - n + 1
            cnt += 1
    return cnt

print(strStr(txt, pat))

# solution3: 滑动窗口(双指针)