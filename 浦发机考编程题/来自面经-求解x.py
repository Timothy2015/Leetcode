# 题目描述：
# 数字x满足 1000<= x <= 9999且 x%a=0, (x+1)%b=0, (x+2)%c=0，现给定abc的值，求x

# 答案参考：https://blog.csdn.net/FANGLICHAOLIUJIE/article/details/100060084

def findX(a, b, c):
    res = []
    for x in range(1000,10000):
        if x%a==0 and (x+1)%b==0 and (x+2)%c==0:
            res.append(x)
    return res

print(findX(10,3,1)) # 1028
# print(findX(1,2,3)) # 1003
# print(findX(1,1,1)) # 1003