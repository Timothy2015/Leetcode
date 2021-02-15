# https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/

class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 优化边界的处理
        s = list('#' + s + '#')
        for i in range(1, len(s)-1):
            if s[i]=='?':
                temp = 122
                while temp == ord(s[i-1]) or temp==ord(s[i+1]):
                    temp -= 1
                s[i] = chr(temp)
        # 切片：[a,b),左闭右开区间
        return ''.join(s[1:-1])

        """
        if s=='': return s
        if len(s)==1 and s=='?': return 'z'
        # 转化为字符列表
        s = list(s)
        i = 0
        while i < len(s):
            temp = 122
            if s[i] == '?':
                if i==0:
                    while temp == ord(s[i+1]):
                        temp -= 1
                    s[i] = chr(temp)
                elif i==len(s)-1:
                    while temp == ord(s[i-1]):
                        temp -= 1
                    s[i] = chr(temp)
                else:
                    while chr(temp)==s[i-1] or chr(temp)==s[i+1]:
                        temp -= 1
                    s[i] = chr(temp)
            i += 1
        return ''.join(s)
        """

    # 聪明的方式处理边界：首尾添加特殊字符‘#’
    """
    def modifyString(self, s):
        # 下面一行代码是亮点
        s = list("#" + s + "#")
        for i in range(1, len(s)-1):
            if s[i] == "?":
                for j in range(97, 123):
                    if chr(j) != s[i+1] and chr(j) != s[i-1]:
                        s[i] = chr(j)
                        break
        return "".join(s[1:-1])
    """
