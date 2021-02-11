# https://leetcode-cn.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ## 滑动窗口 - 解题模板
        """该题特点：子串要求连续，目标窗口大小等于len(s1)"""
        # 1. 初始化need, window计数器
        need = collections.Counter()
        window = collections.Counter()
        for c in s1:
            need[c] += 1
        # 2. 双指针left, right,左闭右开区间[left,)
        left = 0; right = 0
        valid = 0 
        length = len(s1)
        # 3. 滑动扩大窗口
        while right < len(s2):
            c = s2[right]
            right += 1
            if need[c]:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            # 当长度相等时，缩小窗口： 先减一个，方便后面再加一个
            print(right - left + 1)
            # if right-left+1 == length: # [left, right)
            if right - left == length:
                if valid == len(need):
                    return True
                
                d = s2[left]
                left += 1
                if need[d]:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return False


