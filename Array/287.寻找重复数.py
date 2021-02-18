# https://leetcode-cn.com/problems/find-the-duplicate-number/

# 二分查找题解：https://leetcode-cn.com/problems/find-the-duplicate-number/solution/er-fen-fa-si-lu-ji-dai-ma-python-by-liweiwei1419/

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## 最佳的目标解法：二分查找
        size = len(nums)
        left = 1
        right = size - 1

        while left < right:
            mid = left + (right - left) // 2

            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            # 根据抽屉原理，小于等于 4 的数的个数如果严格大于 4 个，
            # 此时重复元素一定出现在 [1, 4] 区间里

            if cnt > mid:
                # 重复的元素一定出现在 [left, mid] 区间里
                right = mid
            else:
                # if 分析正确了以后，else 搜索的区间就是 if 的反面
                # [mid + 1, right]
                left = mid + 1
        return left

        ## 初阶方案：原地排序再遍历
        """
        # 原地排序
        nums.sort() #快排的时间复杂度：O(N*LogN)
        # print(nums)
        # 遍历寻找重复数
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
        """
        ## 进阶：1.证明nums中至少存在一个重复的数字
        """
        # 哈希表
        h = {}
        for i in nums:
            h[i] = i
        print(len(h))
        print(len(nums))
        return len(h)<len(nums)
        """
        # 遍历数组放入哈希表/集合中，以数字为键，哈希表/集合长度小于数组长度，则至少存在一个重复的数字
        """
        # 集合
        s = set() # 创建一个空集合，必须使用set()
        for i in nums:
            if i in s:
                return i
            else:
                s.add(i)
        """

