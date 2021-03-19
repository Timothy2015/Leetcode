# https://leetcode-cn.com/problems/combinations/

# 解法二：回溯算法 + 剪枝
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯算法
        # 1.路径：已经做出的选择
        # 2.选择列表：可以做出的选择
        # 3.结束条件：到达决策树的底部 或 题目的限定条件
        if k <= 0 or k > n:
            return [] 

        nums = []
        for i in range(1, n+1):
            nums.append(i)
        # print(nums)

        def backTrace(trace, begin, nums):
            # 如何去重？[1,2], [2,1]

            # 结束条件
            if len(trace) == k:
                # temp = sorted(trace)
                # print(trace)
                # if temp not in res:
                res.append(trace[:])
            
            # 遍历递归条件
            for i in range(begin, len(nums)):
                # 跳过已经做出的选择
                # if nums[i] in trace:
                    # continue
                
                # 递归之前：做出选择
                trace.append(nums[i])
                backTrace(trace, i+1, nums)
                # 递归之后：撤销选择
                trace.pop()
        
        res = []
        trace = []
        backTrace(trace, 0, nums)
        return res


# 解法一：回溯算法下的暴力求解，套用模板（超出时间限制）
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 回溯算法
        # 1.路径：已经做出的选择
        # 2.选择列表：可以做出的选择
        # 3.结束条件：到达决策树的底部 或 题目的限定条件

        nums = []
        for i in range(1, n+1):
            nums.append(i)
        # print(nums)

        def backTrace(trace, nums):
            # 如何去重？[1,2], [2,1]

            # 结束条件
            if len(trace) == k:
                temp = sorted(trace)
                # print(trace)
                if temp not in res:
                    res.append(temp[:])
            
            # 遍历递归条件
            for i in range(len(nums)):
                # 跳过已经做出的选择
                if nums[i] in trace:
                    continue
                
                # 递归之前：做出选择
                trace.append(nums[i])
                backTrace(trace, nums)
                # 递归之后：撤销选择
                trace.pop()
        
        res = []
        trace = []
        backTrace(trace, nums)
        return res
"""