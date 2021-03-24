# 字符串的反转输出

print("input a string: ")
str = input()

def reverseStr(str):
    res = ''
    for i in range(len(str)-1, -1, -1):
        res += str[i]
    return res

print(reverseStr(str))