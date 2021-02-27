# 题目描述：
# 合并有序数组，排序并去掉重复的数字（注意：是删除，不是把重复的变成一个，不然只过50%）：
# 如输入1 2 3、2 5 6输出1 3 5 6

"""关键理解：去重，不是把重复的变成一个，而是全部删除 --- 测试用例会告诉你这一点"""

nums1 = [1,2,3,4,8]
nums2 = [2,5,6,7]

def mergeOrderedLists(nums1, nums2):
    # 判空处理
    if not nums1: return nums2
    if not nums2: return nums1

    # 合并数组
    res = [] 
    fir = sec = 0
    while fir < len(nums1) and sec < len(nums2):
        if nums1[fir] < nums2[sec]:
            res.append(nums1[fir])
            fir += 1
        elif nums1[fir] == nums2[sec]:
            # 重复的全部去掉
            fir += 1
            sec += 1
        else:
            res.append(nums2[sec])
            sec += 1
    while fir < len(nums1):
        res.append(nums1[fir])
        fir += 1
    while sec < len(nums2):
        res.append(nums2[sec])
        sec += 1
    return res

print(mergeOrderedLists(nums1, nums2))