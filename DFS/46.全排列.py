# https://leetcode-cn.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # 自定义简单的列表切片函数
        def self_slice(nums, l, r):
            # [l, r)
            res = []
            for i in range(l, r):
                res.append(nums[i])
            return res

        # 回溯算法
        def backTrace(nums, trace): # 路径 + 选择
            # 结束条件
            if len(trace) == len(nums):
                # res.append(trace) # 这里是添加的list的地址
                # res.append(trace[:])
                # python不能用切片
                res.append(self_slice(trace, 0, len(trace)))
                return
            
            # 核心代码：递归前后的操作
            for i in range(len(nums)):
                # 重复的跳过(后面改进为哈希表，查找时间O(1))
                if nums[i] in trace:
                    continue

                # 递归之前做选择
                trace.append(nums[i])
                # print(trace)
                backTrace(nums, trace)
                # 递归之后撤选择
                trace.pop()

        res = []
        trace = []
        backTrace(nums, trace)
        # res = copy.deepcopy(res) # 在这里进行深浅拷贝没有用
        return res

        # 时间复杂度O(n!)