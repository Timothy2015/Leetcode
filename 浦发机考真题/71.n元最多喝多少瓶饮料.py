# 题型一：
# 一块钱一瓶饮料，两个饮料瓶可以再换一瓶，问有n元钱最多可以喝几瓶？

# n = map(int, input())

## 递推公式：f(n) = 2*n -1
# f(1) = 1
# f(2) = 2+1 = 3
# f(3) = 3+2 = 5
# f(4) = 4+3 = 7
def maxN(n):
    return 2*n - 1

## 递归求解
def maxN_r(n):
    if n==1:
        return 1
    # 多一块钱意味着什么：最后一定都剩一个空瓶的
    # 1元 => 1瓶 + 1空瓶，与之前的1空瓶组合，带来2瓶 + 1空瓶
    # f(n) = f(n-1) + 2
    return maxN_r(n-1) + 2

print(maxN_r(20)) # 39
print(maxN_r(10)) # 19

