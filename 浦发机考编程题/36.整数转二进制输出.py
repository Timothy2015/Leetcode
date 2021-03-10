# 整数转二进制输出

def dec2Bin(n):
    strs = bin(n)
    res = ""
    for i in range(2, len(strs)):
        res += strs[i]
    return int(res)
    # return res

# n = 1234
n = 5
print(dec2Bin(n))