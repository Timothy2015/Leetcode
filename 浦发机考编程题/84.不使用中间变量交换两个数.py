# 问题：
# 不使用中间变量，交换两个数的值

def swap(a, b):
    # 注意：无需转换为二进制

    # 交换操作，使用异或^运算
    a = a ^ b
    b = a ^ b
    a = a ^ b

    return (a, b)

a = 3
b = 5
print(swap(a, b))

