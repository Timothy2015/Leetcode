# https://leetcode-cn.com/problems/remove-duplicate-letters/

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # 计数器
        count = collections.Counter()
        for c in s:
            count[c] +=1 
        
        # 一个list，模拟实现栈
        stack = []
        for c in s:
            # 遍历一个字符，计数器减一
            count[c] -= 1

            # 如果字符串已经入栈，直接跳过
            """这样就可以避免改变相对顺序了"""
            if c in stack: continue
            # print(c)
            
            # 如果栈不空，且c小于栈顶的元素，出栈前面所有的重复字符
            """关键代码：
            1. 什么时候停止pop，栈顶元素已唯一时
            2. 推荐使用while循环，启动出栈的开关始终是stack[-1] > c
            """
            ## 错解一
            # while stack and stack[-1] > c:
            #     if count[stack[-1]] !=0:
            #         stack.pop()
            # 错解二
            # if stack and stack[-1] > c:
            #     # 有一个逆序，就要遍历栈，出栈所有重复字符
            #     # * 这个思路错误，会改变相对顺序
            #     # * 这样就绕进去了，不停的修修补补，没完没了
            #     for i in range(len(stack)-1, -1, -1):
            #         if count[stack[i]] == 0:
            #             break
            #         stack.pop()
            ## 正解
            while stack and stack[-1] > c:
                # 若之后不再存在栈顶元素了，停止pop
                if count[stack[-1]] == 0:
                    break
                stack.pop()
            
            if c not in stack:
                stack.append(c)
        
        return "".join(stack)



# java代码
"""
class Solution {
    public String removeDuplicateLetters(String s) {
        Stack<Character> stk = new Stack<>();

        // 维护一个计数器记录字符串中字符的数量
        // 因为输入为 ASCII 字符，大小 256 够用了
        int[] count = new int[256];
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i)]++;
        }

        boolean[] inStack = new boolean[256];
        for (char c : s.toCharArray()) {
            // 每遍历过一个字符，都将对应的计数减一
            count[c]--;

            if (inStack[c]) continue;

            while (!stk.isEmpty() && stk.peek() > c) {
                // 若之后不存在栈顶元素了，则停止 pop
                if (count[stk.peek()] == 0) {
                    break;
                }
                // 若之后还有，则可以 pop
                inStack[stk.pop()] = false;
            }
            stk.push(c);
            inStack[c] = true;
        }

        StringBuilder sb = new StringBuilder();
        while (!stk.empty()) {
            sb.append(stk.pop());
        }
        return sb.reverse().toString();
    }
}
"""