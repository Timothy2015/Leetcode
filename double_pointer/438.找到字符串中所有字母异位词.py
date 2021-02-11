# https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 滑动窗口 - 解题模板
        res = []
        # 1.初始化need, window计数器
        need = collections.Counter()
        window =  collections.Counter()
        for c in p:
            need[c] += 1
        # 2.双指针区间：[left, right)
        left = 0; right = 0
        valid = 0
        lenght = len(p)
        # 3.滑动right,增大窗口
        while right < len(s):
            c = s[right]
            right += 1
            if need[c]:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            # [left, right)长度等于lenght,缩小窗口
            if right - left == lenght:
                if valid == len(need):
                    res.append(left)
                
                d = s[left]
                left += 1
                if need[d]:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res