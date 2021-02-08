# https://leetcode-cn.com/problems/longest-palindrome/

# 重要工具：python3的计数器
import collections
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 计数器
        c = collections.Counter()
        # s可以直接当成字符串数组访问
        for i in range(len(s)):
            c[s[i]] += 1
        res = 0
        for char in c:
            # print(c[char])
            if c[char] % 2 ==0:
                res += c[char]
            if c[char] % 2 ==1: # 反馈的测试用例：“ccc”
                res += c[char]-1
        if res < len(s):
            res += 1
        return res

"""用时最短的例子"""
class Solution1:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if v % 2 == 1 and ans % 2 == 0:
                ans += 1
        return ans
