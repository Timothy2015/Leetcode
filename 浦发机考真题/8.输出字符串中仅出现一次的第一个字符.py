# 输出字符串中仅出现一次的第一个字符
# str.count()

def printOnlyFirst(s):
    if s=='': return s
    for c in s:
        if s.count(c)==1:
            print(c)
            break
    return ''

printOnlyFirst('abcdabcdg')