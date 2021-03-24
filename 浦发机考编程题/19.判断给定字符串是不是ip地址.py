# 判断给定字符串是否为合法ip地址：
# 判断 Ip 地址是否合法， 如 128.211.11.2 将字符串分为 128 211 11 2 四个整形变量，
# 判断范围是否在 0~255 之间， 若有一个不在范围内， 则为不合法

print("input a string:")
str = input()

def isIP(str):
    strs = str.split(".")
    for s in strs:
        if s<'0' or s>'255':
            return False
    return True

print(isIP(str))