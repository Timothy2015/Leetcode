# https://leetcode-cn.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 回溯算法
        # 1. 路径：已经做出的选择
        # 2. 选择列表：可以做的的选择
        # 3. 结束条件：到底绝对的底层 或 满足题目的限定条件

        res = []
        trace = []
        def backTrace(nums, start, trace):
            # 结束条件——此处没有，循环结束，就结束了
            # 什么时候添加结果？每一步的中间状态都是子集，都需要添加
            res.append(trace[:]) # 需要复制值，添加切片操作

            # res.append(trace) # 浅拷贝， 得不到正确结果

            # 子集不能重复，所以引入start参数
            for i in range(start, len(nums)):
                trace.append(nums[i])
                # backTrace(nums, start+1, trace)
                backTrace(nums, i+1, trace)
                trace.pop()
        
        backTrace(nums, 0, trace)
        return res
        


            
