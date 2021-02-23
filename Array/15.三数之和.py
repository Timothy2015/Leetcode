# https://leetcode-cn.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 排序(不能去重，因为有[-1, -1, 2])
        nums.sort()

        # 辅助函数：二分查找
        def find(nums, l, r, target):
            temps = []
            while l < r:
                if nums[l]+nums[r] == (-target):
                    # [-2,0,2], [-2,1,1]
                    if [target, nums[l], nums[r]] not in temps:
                        temps.append([target, nums[l], nums[r]])
                    r -= 1
                    l += 1
                elif nums[l]+nums[r] > (-target):
                    r -= 1
                else:
                    l += 1
            return temps
        # 遍历二分
        """
        优化重点：如何去除重复解（not in 方式太低效）
            ————跳过重复的target
        """
        res = []
        for i in range(len(nums)-2):
            ##### 高效去重，跳过重复的target
            # 落网之鱼：[-2, 0, 0, 2, 2],两个[-2,0,2]
            if i>0 and nums[i]==nums[i-1]:
                continue
            ##### 剪枝提速: 数组有序号，nums[i]大于则没有结果了
            if nums[i] > 0:
                continue
            temps = find(nums, i+1, len(nums)-1, nums[i])
            for temp in temps:
                # if temp and (temp not in res):
                res.append(temp)
        return res

# 剪枝之后：
# 4168ms ---> 496ms

