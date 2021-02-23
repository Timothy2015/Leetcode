# https://leetcode-cn.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 恰好有两个元素只出现一次
        ## 最佳解法：分组异或
        
        # 设两个只出现一次的数为a和b, res = a ^ b
        res = functools.reduce(lambda x,y:x^y, nums)

        # 如何分组异或，找到res（如果res=0,意味着a=b，不可能）中任意一个为1的位，用它来分组
        ## 原因：1 & 1 = 1; 1 & 0 = 0, 1可以把0和1区分开，即可以按照那个为1的为将数组分为两组
        # 假设 a=010 b=110
        ## 进深理解：过程中也将a和b区分开了，因为a和b那个位一定不同，异或出来的结果才为1
        # 假设 res = 100
        # 那么 div = 001
        #            010
        #            100 (while循环结束，找到了最低位为1的位置)
        div = 1
        while res & div == 0:
            div <<= 1 
        
        # 利用div划分两个数组，一个包含a，另一个包含b
        # 其他出现两次的数，不同时在第一组，就同时在第二组，因为第3位不是同为0，就是同为1
        a = b = 0
        for num in nums:
            if num & div:
                a ^= num
            else:
                b ^= num 
        return [a,b]
        
        ## 空间复杂度O(N)，使用set去重计算 或 hashmap计数


