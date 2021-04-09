# 题目描述
# * 给定数列a, 按全排列顺序打印数列

# leetcode-46.全排列（回溯算法）
# https://leetcode-cn.com/problems/permutations/

"""
# 回溯算法的关键步骤：
1. 路径：已经做出的选择
2. 选择列表：可以做出的选择
3. 结束条件：选择列表为空，或已经达到决策树的底部
"""
nums = [1, 2, 3]
"""
# 使用python不能使用切片，自定义切片列表的切片
def list_slice(nums, l, r):
    res = []
    for i in range(l, r):
        res.append(nums[i])
    return res

res = []
def backTrace(trace, nums):
    # 结束条件
    if len(trace) == len(nums):
        # res.append(trace) # 浅拷贝（测试之后才知道问题所在）
        # res.append(trace[:]) # 需要复制值，而非引用
        res.append(list_slice(trace, 0, len(trace)))
        # 反弹回去，结果通过res返回，这里无需返回值
        return 

    # 核心代码：递归前后的操作
    # 遍历寻找列表
    for i in range(len(nums)):
        # 跳过已经做出的选择
        
        if nums[i] in trace:
            continue

        # 递归前：做出选择
        trace.append(nums[i])
        backTrace(trace, nums)
        # 递归后：撤销选择
        trace.pop()

trace = []
backTrace(trace, nums)
print(res)
"""


# 回溯算法的时间复杂度：O(N!)
"""
局部时间复杂度优化：这里的 if nums[i] in trace 的查找效率为O(n),可以减低为O(1)
* 使用哈希表
* 实践情况：因为不太熟悉字典的操作
  * 中间加入了for循环重构列表，连局部的时间复杂度都没有得到改进
"""

# python的字典:
# dict.items() 以列表返回可遍历的（键，值）元组数组
# dict.keys() 以列表返回一个字典所有的键
# dict.values() 以列表返回字典中所有的值

import collections

trace = collections.OrderedDict()

def backTrace(trace, nums):
    # 结束条件
    if len(trace.keys()) == len(nums):
        temp = []
        for key in trace.keys():
            temp.append(key)
        res.append(temp)
        return
    
    # 遍历选择列表
    for i in range(len(nums)):
        # 跳过已经做出的选择
        if nums[i] in trace:
            continue
        
        # 递归前：做出选择
        trace[nums[i]] = nums[i]
        backTrace(trace, nums)
        # 递归后：撤销选择
        trace.popitem()

res = []
backTrace(trace, nums)
print(res)










