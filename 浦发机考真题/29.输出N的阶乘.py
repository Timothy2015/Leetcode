# 0! = 1 （人为定义，为了相关公式的表述及运算更方便）
# 1! = 1
# 2! = 1*2 = 2
# 3! = 1*2*3 = 6


# 输出N的阶乘
def printOrderOfN(n):
    # 输入校验
    if n < 0: print('n必须为非负数，请重新输入！')
    # 当n==0, 规定0!= 1
    elif n==0: 
        print('0! = 1')
    # 当n > 0
    else:
        res = 1
        for i in range(1, n+1):
            res *= i 
        print("{}! = {}".format(n, res))

# printOrderOfN(0)
printOrderOfN(2)
printOrderOfN(4)
printOrderOfN(9)
