# https://leetcode-cn.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快速双指针的变体
        # fast = 0; slow = 0
        # count = 0
        # while fast < len(nums):
        #     if nums[fast] != 0:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #         count += 1
        #     fast += 1
        # while count < len(nums):
        #     nums[count] = 0
        #     count += 1

        """标准解法依然有效，并且更好！只需遍历一次"""
        fast = 0; slow = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1



class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快速双指针的变体
        # fast = 0; slow = 0
        # count = 0
        # while fast < len(nums):
        #     if nums[fast] != 0:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #         count += 1
        #     fast += 1
        # while count < len(nums):
        #     nums[count] = 0
        #     count += 1

        """标准解法依然有效，并且更好！只需遍历一次"""
        fast = 0; slow = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1



iclass Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 快速双指针的变体
        # fast = 0; slow = 0
        # count = 0
        # while fast < len(nums):
        #     if nums[fast] != 0:
        #         nums[slow] = nums[fast]
        #         slow += 1
        #         count += 1
        #     fast += 1
        # while count < len(nums):
        #     nums[count] = 0
        #     count += 1

        """标准解法依然有效，并且更好！只需遍历一次"""
        fast = 0; slow = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1


