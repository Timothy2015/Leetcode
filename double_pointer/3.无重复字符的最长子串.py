# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## 滑动窗口 - 解题模板
        # res = []
        res = 0 
        # 1. 初始化need, windonw计数器
        # need = collections.Counter()
        window = collections.Counter()
        # 2. 双指针区间：[left, right)
        left = 0; right = 0
        # 3. 移动right, 扩大窗口
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            # 有重复的时候，移动left, 缩小窗口
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            # res.append(right - left)
            """难点：什么时候统计长度？好保证没有遗漏"""
            # ---1.没有重复的时候，需要更新res
            # ---2.有了重复，去重之后才能计算长度，更新res
            res = max(res, right - left)

        # return max(res) if res else 0
        return res
