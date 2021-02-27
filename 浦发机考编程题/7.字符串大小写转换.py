# 字符串大小写转换
# * 题意理解：将一个字符串中的大写字母转换成小写字母，同时将原有的小写字母转换成大写字母，输出转换后的字符串

# 小写字母 'a'~'z': 97~122
# 大写字母 'A'~'Z': 65~90
def modifyString(s):
    if s=='': return s
    s = list(s)
    for i in range(len(s)):
        # if ord(s[i])>=97 and ord(s[i])<=122:
        if s[i]>='a' and s[i]<='z':
            s[i] = s[i].upper()
        # elif ord(s[i])>=65 and ord(s[i])<=98:
        elif s[i]>='A' and s[i]<='Z':
            s[i] = s[i].lower()
    return ''.join(s)

print(modifyString('abcDEF'))

