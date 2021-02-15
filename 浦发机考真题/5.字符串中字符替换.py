def modifyString(s):
    if s=='': return s
    # string是常量，不能修改，转化为list再处理
    s = list(s)
    i = 0
    while i<len(s):
        if s[i]=='a' or s[i]=='A':
            s[i]='c'
        i += 1
    return ''.join(s)

# TDD
print(modifyString('aAbfA'))
print(modifyString(''))
print(modifyString('aAA'))
print(modifyString('AA'))
    