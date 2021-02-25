# 题型二：
# 1块钱可以买1瓶汽水，2个空瓶可以换一瓶汽水，3个瓶盖可以换一瓶汽水，问：20块可以买到多少瓶汽水


## 迭代递推公式：f(n) = ??
# f(1) = 1
# f(2) = 2+1+1 = 4
# f(3) = 3+8 = 11
# f(4) = 9+8 = 17
# f(5) = 6 + f(4) = 23
# f(6) = 6 + f(5) = 29
# f(7) = 6 + f(6) = 35
def maxN(n):
    if n==1: return 1
    if n==2: return 4
    if n==3: return 11
    res = 11
    for i in range(4, n+1):
        res += 6
    return res

print(maxN(3))
print(maxN(4))
print(maxN(5))


## 递归求解
def maxN_r(n):
    if n==1: return 1
    if n==2: return 4
    if n==3: return 11
    # [有了3个瓶盖之后] 多一块钱意味着什么？-- 此后每次都剩 1空瓶+2瓶盖
    # 1元 => 带来1瓶 + 1空瓶 + 1瓶盖  and 之前1空瓶,2瓶盖
    #     => 带来2瓶 + 2空瓶 + 2瓶盖
    #     => 带来1瓶 + 1空瓶 + 3瓶盖
    #     => 带来1瓶 + 2空瓶 + 1瓶盖
    #     => 带来1瓶 + 1空瓶 + 2瓶盖
    
    # f(n) = f(n-1) + 6
    return maxN_r(n-1) + 6

print(maxN_r(4)) # 

