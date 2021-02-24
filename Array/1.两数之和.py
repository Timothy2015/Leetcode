# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## 二、哈希表 将一个O(N)的查找时间降低为O(1)
        # 哈希表：（val: idx)
        mp = collections.defaultdict(int)
        for i in range(len(nums)):
            # 查找target - x 是不是在hash表中
            # 还要避免使用重复使用同一个元素
            if target - nums[i] in mp:
                return [i, mp[target-nums[i]]]
            mp[nums[i]] = i

        ## 一、暴力枚举 O(N^2)
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == target - nums[j]:
                    return [i,j]
        """
                