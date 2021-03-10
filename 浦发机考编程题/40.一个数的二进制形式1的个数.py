# 题目描述
# 输入一个数字，判断该数字代表的二进制有多少个1，例如输入为7，输出为3

def countOne(n):
    # python不能使用切片
    strs = bin(n)
    count = 0
    for str in strs:
        if str == '1':
            count += 1
    return count

# test
print("input a integer: ")
# n = int(input())
n = 1234
print(countOne(n))
n = 9
print(countOne(9))
