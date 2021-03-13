# 字符串移除奇数位置上的字符

print("input a string: ")
str = input()

def omitOddBit(str):
    new_str = ''
    # 第一个奇数位1，对应下标为0
    for i in range(1, len(str), 2):
        new_str += str[i]
    return new_str

print(omitOddBit(str))