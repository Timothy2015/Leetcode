# https://leetcode-cn.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        # 问题1：如何判断两个括号是否匹配呢？
        ## 关键理解到：用“右括号 ] ” 和“左括号 [”匹配
        # * 也就是遇到了右括号]，就要开始考虑匹配的问题（——回答了什么时候开始考虑匹配——）
        mp = {
            ']':'[',
            '}':'{',
            ')':'('
            # '[':']',
            # '{':'}',
            # '(':')', 
        }

        # 问题2：栈，用list模拟栈，执行匹配过程
        stack = []
        for c in s:
            if c not in mp:
                stack.append(c)
            else:
                # 还有右括号没匹配，栈已空，肯定无效
                if not stack:
                    return False
                # 不空才出栈并比较
                else:
                    if mp[c] != stack.pop():
                        return False
        return stack==[]

        ## 解法二：
        """
        dic = {
            '(':')',
            '[':']',
            '{':'}',
            '?':'?'
        }
        # 列表直接模拟栈就好（此处只用到栈的部分操作）
        stack1 = ['?'] # 巧妙处理栈空时需要出栈的情况，简化代码逻辑
        for c in s:
            if c in dic:
                stack1.append(c)
            else:
                if c != dic[stack1.pop()]:
                    return False
                    
        return len(stack1)==1
        """