# 题型三：
# 2个饮料瓶可以换1瓶饮料，4个瓶盖可以换1瓶饮料，1瓶饮料1块钱，问10块钱最多能买喝几瓶饮料

"""4个瓶盖的时候，更快呈现规律
* 因为当n=2的时候，已经出现了 1空瓶 + 3瓶盖 的瓶颈
* 且当n=3,4,5时，均呈现同样的 剩余瓶颈现象
"""
## 迭代递推公式：f(n) = ??
# f(1) = 1
# f(2) = 3
# f(3) = 7
# f(4) = 11
# f(5) = 15
def maxN(n):
    if n==1: return 1
    if n==2: return 3
    res = 3
    for i in range(3, n+1):
        res += 4
    return res

print(maxN(3))
print(maxN(4))
print(maxN(5))


## 递归求解
def maxN_r(n):
    if n==1: return 1
    if n==2: return 3
    # [当n=2时，出现“剩余瓶颈”] 多一块钱意味着什么？-- 此后每次都剩 1空瓶+2瓶盖
    # 1元 => 带来1瓶 + 1空瓶 + 1瓶盖  and 之前1空瓶,2瓶盖
    #     => 带来2瓶 + 2空瓶 + 2瓶盖
    #     => 带来1瓶 + 1空瓶 + 3瓶盖
    
    # f(n) = f(n-1) + 4
    return maxN_r(n-1) + 4

print(maxN_r(3)) # 
print(maxN_r(4)) # 
print(maxN_r(10)) # 

