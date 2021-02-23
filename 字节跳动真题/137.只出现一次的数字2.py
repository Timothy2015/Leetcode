# https://leetcode-cn.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 空间O(1)的方法：三、位运算（好像开关的跳变），非常巧妙
        seen_once = seen_twcie = 0
        for num in nums:
            seen_once = ~seen_twcie & (seen_once ^ num)
            seen_twcie = ~seen_once & (seen_twcie ^ num)
        return seen_once
        
        # 额外空间O(N):二、使用hashmap(dict)计数，数量为1的即是
        """
        mp = collections.Counter(nums)
        for num in nums:
            if mp[num] == 1:
                return num
        """

        # 额外空间O(N):一、使用set去重计算
        ## 3(a+b+c) - (3a+3b+c) = 2c
        # return (3*sum(set(nums)) - sum(nums)) // 2
