# 给出 A,B 两个字符串， 求在第一个字符串出现， 但第二个字符串中未出现，
# 重复出现时只取第一次出现， 输出字符串

def printString(s, t):
    if s=='': return s
    # if t=='': return s # 错误，s中重复的字符只取第一个

    res = []
    for c in s:
        if c not in t:
            if c not in res:
                res.append(c)
    return ''.join(res)

print(printString('abCCbea', 'adg'))
