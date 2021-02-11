# https://leetcode-cn.com/problems/reverse-string/
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # 双指针：一首一末，反转字符串
        i = 0
        j = len(s)-1
        while i<=j :
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1