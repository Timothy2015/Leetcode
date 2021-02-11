# https://leetcode-cn.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢双指针的变体
        # 特点：倒着来遍历
        fast = len(nums) - 1
        slow = len(nums) - 1
        while fast >= 0:
            if nums[fast] == val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow -= 1
            fast -= 1
        return slow+1