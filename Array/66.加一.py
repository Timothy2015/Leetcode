# https://leetcode-cn.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 关键：处理进位
        """
        # for i in range(len(digits)-1, -1, -1): # 数组长度可能变化，使用while
        i = len(digits)-1
        carry = 0
        temp = 1
        while i >= 0:
            sum = digits[i] + temp + carry
            # carry用后清零
            carry = 0
            # 最后一位：+ 1 + carry (case1)
            if sum > 9:
                # carry-进位
                digits[i] = 0
                carry = 1
                temp = 0
            else:
                digits[i] += 1
            
            # 其他位 + carry (case2)

            i -= 1

            # 无进位，结束循环
            if carry == 0:
                break

        if carry != 0:
            # list在指定位置插入 insert(index, obj)
            digits.insert(0, 1)
        return digits
        """
        

        # 更简洁的python代码
        for i in range(len(digits) - 1, -1, -1):
            digits[i] = (digits[i] + 1) % 10
            # 如果没有产生新的进位，直接结束返回结果
            if digits[i] != 0:
                return digits
        return [1] + digits
        #"""

        # java 版本
        """
        class Solution {
            public int[] plusOne(int[] digits) {
                for (int i = digits.length - 1; i >= 0; i--) {
                    digits[i]++;
                    digits[i] = digits[i] % 10;
                    if (digits[i] != 0) return digits;
                }
                digits = new int[digits.length + 1];
                digits[0] = 1;
                return digits;
            }
        }
        """