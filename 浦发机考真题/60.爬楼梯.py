# 爬一个或者两个台阶， 输入 1 <= n < 90 的数字为台阶数， 
# 以输入 0 作为结束标志， 输出 n 个台阶共有多少种上楼方式

## 动态规划（带有备忘录的枚举） or 递归求解/迭代求解

while True:
    # n = map(int, input())
    n = int(input())

    if n==0:
        break
    if n>=1 and n<90:
        # f(n) = f(n-1) + f(n-2)
        if n==1:
            print("1级台阶上楼的方式：", 1)
        elif n==2:
            print("2级台阶上楼的方式：", 2)
        else:
            n_1 = 1
            n_2 = 2
            n_n = 0
            for i in range(3, n+1):
                n_n = n_1 + n_2
                n_1 = n_2
                n_2 = n_n
            print("{}级台阶上楼的方式：{}".format(n, n_n))
    else:
        print("n为整数，且n的范围为[1,90),您的输入有误，请重新输入!")