# 题目描述
# * 判断单词apple，是否再嵌套列表里，是则计数加1
# * 如[ ['apple', 'b', 'c'], ['apple'], ['b', 'c']], 结果为2

case1 = [['apple', 'b', 'c'], ['applE'], ['b', 'c']]
case2 = [['apple', 'b'], ['b', 'c'], ['apple', 'apPle','Apple']]

def countWord(nums):
    if not nums: return 0
    # 是否区分大小写：这里是区分
    # count = 0
    # for num in nums:
    #     for n in num:
    #         if n=='apple':
    #             count += 1

    # 版本2：不区分大小写
    count = 0
    for num in nums:
        for n in num:
            if n.lower()=='apple':
                count += 1
    return count

print(countWord(case1))
print(countWord(case2))

