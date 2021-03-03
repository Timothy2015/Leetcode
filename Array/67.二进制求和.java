// https://leetcode-cn.com/problems/add-binary/
// 官方题解 https://leetcode-cn.com/problems/add-binary/solution/er-jin-zhi-qiu-he-by-leetcode-solution/

class Solution {
    public String addBinary(String a, String b){
        // StringBuffer is powerful
        StringBuffer ans = new StringBuffer();

        int n = Math.max(a.length(), b.length()), carry = 0;
        for (int i=0; i < n; i++){
            carry += i < a.length() ? (a.charAt(a.length() - 1 -i) - '0') : 0;
            carry += i < b.length() ? (b.charAt(b.length() - 1 -i) - '0') : 0;
            ans.append((char)(carry % 2 + '0'));
            carry /= 2;
        }
        if (carry > 0){
            ans.append('1');
        }
        ans.reverse();
        return ans.toString();
    }
}

"""
class Solution {
    public String addBinary(String a, String b) {
        //自带的函数 (java无法通过全部测试用例)
        return Integer.toBinaryString(
            Integer.parseInt(a,2) + Integer.parseInt(b,2)
        );
        /*
        在 Java 中:
        如果字符串超过 3333 位，不能转化为 Integer
        如果字符串超过 6565 位，不能转化为 Long
        如果字符串超过 500000001500000001 位，不能转化为 BigInteger
        因此，为了适用于长度较大的字符串计算，我们应该使用更加健壮的算法。
        */
    }
}
"""