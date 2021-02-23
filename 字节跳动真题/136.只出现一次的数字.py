# https://leetcode-cn.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            # py3的异或运算符^
            res ^= i
        return res