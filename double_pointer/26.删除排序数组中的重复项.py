# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ## 投机取巧失败 - 需要原地修改
        # arr = [i for i in set(nums)]
        # return len(arr)
        
        """没刷过就不知道怎么做啊！多多刷题的重要性"""
        ## 快慢双指针的变体
        slow = 0; fast = 0
        while fast < len(nums):
            if nums[fast] != nums[slow]:
                slow += 1
                # 维护一个nums[0,...,slow]的数组
                nums[slow] = nums[fast]
            fast += 1
        # 返回新数组的长度（我自己并不需要真的做删除操作）
        return slow+1
