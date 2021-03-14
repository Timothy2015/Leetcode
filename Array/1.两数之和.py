# https://leetcode-cn.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 暴力求解，双重for循环 -- O(N^2)
        """
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        """
        
        # 先排序（O(N*logN)），再用双指针(O(N))  -- O(N*logN)
        """这种方法无效！！！，因为是返回下标，不能破坏原来的数组"""
        """
        nums.sort()
        l = 0; r = len(nums)-1
        while l < r:
            sum = nums[l] + nums[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l, r]
        """

        # 哈希表查找 -- O(N)，将其中的一个O(N)复杂度降低为O(1)
        """最优解"""
        mp = {}
        for i in range(len(nums)):
            # 先查找target - nums[i]是否在哈希表中，有则返回下标
            # 没有则添加到哈希表中
            if target - nums[i] in mp:
                return [i, mp[target - nums[i]]]
            # 值:下标
            mp[nums[i]] = i
