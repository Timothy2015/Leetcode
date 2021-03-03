//https://leetcode-cn.com/problems/plus-one/

class Solution {
    public int[] plusOne(int[] digits) {
        //python的快速实现
        /*
        for i in range(len(digits)-1, -1, -1):
            # %模运算 综合产生进位和不产生进位两种情况
            digits[i] = (digits[i] + 1) % 10
            # 如果没有进位，结束；进位的判断看digit[i]是否为0
            if digits[i] != 0:
                return digits
        # 如果原最高位变为0了，增加一位最高位（999 + 1 = 1000）
        if digits[i] == 0:
            # digits.insert(0,1)
            # return digits
            return [1] + digits # 链表的拼接
        */

        //修改上面的代码为java版本（python验证了逻辑）
        for (int i=digits.length-1; i>-1; i--){
            digits[i] = (digits[i] + 1) % 10;
            if (digits[i] != 0){
                return digits;
            }
        }
        int[] nums = new int[digits.length + 1];
        // 临时变量i失效
        // if (digits[i] == 0){
        if (digits[0] == 0){
            //java的数组长度不可变，需要新建一个数组(不能创建在里面，否则外面return无法访问)
            // int[] nums = new int[digits.length + 1];
            nums[0] = 1;
            for (int i=1; i<nums.length; i++){
                nums[i] = digits[i-1];
                // return nums; // 末尾需要有return语句，放在末尾
            }
        }
        return nums;
    }
}

 //java 版本
 """
 疑问：为什么不需要将digits复制一遍到newDigits中？而是一创建就有
        digits[0:n-1] == newDigits[1:n]
 """
class Solution {
            public int[] plusOne(int[] digits) {
                for (int i = digits.length - 1; i >= 0; i--) {
                    digits[i]++;
                    digits[i] = digits[i] % 10;
                    if (digits[i] != 0) return digits;
                }
                // digits = new int[digits.length + 1];
                int[] newDigits = new int[5];
                newDigits[0] = 1;
                // System.out.println(newDigits[1]); // 0
                // System.out.println(newDigits[2]); // 0
                return newDigits;
            }
}