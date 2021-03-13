#  https://leetcode-cn.com/problems/valid-parentheses/submissions/

class Solution:
    def isValid(self, s: str) -> bool:

        if not str: return True

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
        # 什么时候开始匹配，遇到右括号时，需要考虑匹配
        # * 遇到左括号进栈
        # * 遇到右括号，挤出栈顶元素，考虑匹配的问题
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

