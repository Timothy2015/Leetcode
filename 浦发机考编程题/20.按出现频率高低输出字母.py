# 按出现频率高低输出字母， 给出字典序列为 aaabbbbassd

def sortByTimes(str):
    mp = {}
    for c in str:
        if c not in mp:
            mp[c] = 1
        else:
            mp[c] += 1
    res = list(mp.keys())
    # 手写一个冒泡排序: 每次把当前的最大值放到前面(降序)
    # [4, 1, 2, 4]
    for i in range(len(res)-1):
        for j in range(i, len(res)-1):
            if mp[res[j]] < mp[res[j+1]]:
                res[j], res[j+1] = res[j+1], res[j]
    return res

# str = 'aaabbbbassd'
str = input()
print(sortByTimes(str))