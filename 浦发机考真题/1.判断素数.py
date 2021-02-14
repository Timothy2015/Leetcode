# 题目描述
# * 判断素数：除了1和该数本身，没有其他可以整除的数（素数最小为2）
import math
def is_prime(n):
            if n<2: return False
            if n==2: return True
            for i in range(2, int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True

# 简写
def isPrime(n):
    return n>1 and all(n%i!=0 for i in range(2,int(n**.5)+1))


# TDD - 测试
"""
100以内的质数(素数)有2，3，5，7，11，13，17，19，23，29，31，37，41，
43，47，53，59，61，67，71，73，79，83，89，97，在100内共有25个质数。
"""
for i in range(1,101):
    # if is_prime(i):
    if isPrime(i):
        print(i)