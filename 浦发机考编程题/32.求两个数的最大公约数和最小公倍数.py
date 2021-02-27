# 什么是最大公约数和最小公倍数？
# https://www.php.cn/mysql-tutorials-415848.html

n, m = map(int, input().split())

# 最大公约数：枚举求解 (枚举的复杂度可控，为O(N))
def maxComDivisor(n, m):
    n = min(n, m)
    for i in range(n, 0, -1) :
        if n%i==0 and m%i==0:
            return i

print(maxComDivisor(n, m))


# 最小公倍数：公式求解
# * 1. 先求最大公约数
# * 2. 最小公倍数 = 两数之积 / 最大公约数
def minComMultiple(n, m):
    product = n*m
    maxComDiv = maxComDivisor(n, m)
    return product // maxComDiv

print(minComMultiple(n,m))





