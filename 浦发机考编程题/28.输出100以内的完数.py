# 完全平方数：
# 0 = 0 (零也是完全平方数)
# 1 = 1
# 4 = 1 + 3
# 9 = 1 + 3 + 5
# n**2 = 1 + 3 + 5 + ... + 2n-1 

# 输出m以内 (包含m) 的完全平方数
def printPerfectSquare(m):
    if m < 0: print("m必须为非负数，请重新输入！")
    n = 0
    # 包含m
    while n**2 <= m:
        print(n**2)
        n += 1
printPerfectSquare(100)