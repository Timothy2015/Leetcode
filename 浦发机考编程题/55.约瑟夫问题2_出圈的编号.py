# 题目描述：
# https://www.luogu.com.cn/problem/P1996（P1996 约瑟夫问题）

print("input two numbers:")
# n, m = input().split(' ')
n, m = map(int, input().split(' '))

# 解法二：使用队列来模拟
queue = [i for i in range(1, n+1)]
# 遍历的指针
p = 1
while queue:
    # 找到了第m个数，输出并弹出
    if p == m:
        print(queue[0])
        queue.pop(0)
        # p指针置为1，开始下一轮遍历
        p = 1
    else:
        # 遍历到的数字，如果不是，则放到末尾
        queue.append(queue.pop(0))
        # 继续查看下一个数
        p += 1

# 失败的尝试1
"""
visits = [0]*n
# for i in range(1, n+1):
    # nums.append(i)
# 一共需要出圈n次
k = 0
for i in range(n):
    while k < m:
        if k == m-1:
            print()
            s = 1
        if visits[s]==1:
            k -= 1
    print(s)
    visits[s] = True
"""