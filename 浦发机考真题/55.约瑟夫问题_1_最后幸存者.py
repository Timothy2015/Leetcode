"""
第一次在牛客网上刷题并通过（参考了答题区的题解处理输入）
"""

# n,m = input()
n, m = map(int, input().split())
## 递归求解 - 超时
"""
def josephus(n, m):
    if n==1:
        return 0
    return (josephus(n-1, m) + m) % n
# 函数求得的结果为数组下标，需要加1
print(josephus(n, m) + 1)
"""
## 迭代求解
# n=1
live = 0
# n=2,...,n
for i in range(2,n+1):
    live = (live + m) % i 
print(live + 1)