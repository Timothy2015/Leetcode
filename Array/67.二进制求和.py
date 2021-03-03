# https://leetcode-cn.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ## 二进制求和
        # 1.str --> int，并且值为二进制对应的值
        n1 = 0
        for i in range(len(a)):
            n1 = n1*2 + int(a[i])
        n2 = 0
        for i in range(len(b)):
            n2 = n2*2 + int(b[i])
        res = bin(n1 + n2)
        return str(res[2:])

# eval()函数用来执行一个字符串表达式，并返回表达式的值。
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = eval("0b"+a)
        b = eval("0b"+b)
        return bin(a+b)[2:]
"""

# 更简洁的解法 int(x, base) 第二个参数为基，默认十进制
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
"""