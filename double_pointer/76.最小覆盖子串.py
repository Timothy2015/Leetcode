# https://leetcode-cn.com/problems/minimum-window-substring/

# import collections
# import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 滑动窗口 - 解题模板
        # 1.初始化need, window计数器
        need = collections.Counter()
        window = collections.Counter()
        for c in t:
            need[c] += 1
        # 2.双指针left, right, 左闭右开的窗口区间[left, right)
        left = 0; right = 0
        valid = 0 
        # 3.遍历字符串，滑动扩大窗口
        start = 0; length = sys.maxsize
        while right<len(s):
            c = s[right]
            right +=1
            if need[c]:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            # 当找到了覆盖子串时，缩写窗口
            while valid == len(need):
                # 更新覆盖子串的start和len
                if right - left < length:
                    start = left
                    length = right - left
                
                d = s[left]
                left += 1
                if need[d]:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        
        return s[start:start+length] if length!=sys.maxsize else ""
    

