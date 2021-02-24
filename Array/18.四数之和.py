# https://leetcode-cn.com/problems/4sum/

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ## 四数之和转换为三数之和 O(N^3)
        # 三数之和转换为两数之和 O(N^2) --- 排序 + 双指针
        # 两数之和，哈希表查找 O(N) --- 不允许排序（+ 二分查找），因为要求返回下标

        nums.sort() # 原地排序
        
        # a + b = t-d-c
        def twoSum(nums, l, r, target, fir, sec):
            # 有序数组
            temps = []
            while l < r:
                ## Debug
                # print(l, r)
                if nums[l] == target - nums[r]:
                    if [fir, sec, nums[l], nums[r]] not in temps:
                        temps.append([fir, sec, nums[l], nums[r]])  
                    l += 1
                    r -= 1
                elif nums[l] < target - nums[r]:
                    l += 1
                else:
                    r -= 1
            return temps
        
        # a + b = t-d-c        
        # for + for 
        res = []
        for i in range(len(nums)-3):
            # 去重(不能随便去重，因为target不定)
            # if i > 0 and nums[i]==nums[i-1]:
                # continue
            for j in range(i+1, len(nums)-2):
                T = target - nums[i] - nums[j]
                temps = twoSum(nums, j+1, len(nums)-1, T, nums[i], nums[j])
                for temp in temps:
                    if temp not in res:
                        res.append(temp)
        return res