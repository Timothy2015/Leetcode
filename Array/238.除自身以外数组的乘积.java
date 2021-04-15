//https://leetcode-cn.com/problems/product-of-array-except-self/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        // 进阶 时间复杂度为O(n)，空间O(1)
        // 提示： 出于对空间复杂度分析的目的，输出数组不被视为额外空间
        // 思路：使用输出数组res取代中间数组L和R

        int[] res = new int[nums.length];

        // res保存前缀之积
        res[0] = 1;
        for (int i=1; i<nums.length; i++){
            res[i] = res[i-1] * nums[i-1];
        }
        // 获取后缀之积，并直接对应相乘，保存到res中
        // res[res.length-1] 已经是所需要的结果
        /*
        input: 1,  2,  3, 4
        L:     1,  1,  2, 6 (res)
        R:     24, 12, 4, 1
        res:   24, 12, 8, 6
        */
        int R = 1;
        for (int j=nums.length-2; j>=0; j--){
            // temp = res[j+1] / res[j]; //很接近正确思路了：用一个数代替R
            res[j] = res[j] * nums[j+1] * R;
            R *= nums[j+1];
        }
        return res;

        // 不能使用除法，且时间复杂度为O(n)，空间O(n)
        /*
        int[] L = new int[nums.length]; //前缀之积：当前x的左边元素之积
        int[] R = new int[nums.length]; //后缀之和：当前x的右边元素之积
        int[] res = new int[nums.length];

        //首位特殊位置的初始化
        L[0] = 1;
        R[R.length-1] = 1;
        for (int i=1; i<L.length; i++){
            L[i] = nums[i-1] * L[i-1];
        }
        for (int j=R.length-2; j>=0; j--){
            R[j] = nums[j+1] * R[j+1];
        }
        for (int k=0; k<res.length; k++){
            res[k] = L[k] * R[k];
        }

        return res;
        */

        // 解法一：使用除法 + 考虑除数为0的情况（2021-4-11，浦发笔试编程第3题）
        /* 
        先遍历一次，判断0的个数，cnt计数0的个数：
        然后判断：
            cnt>=2，返回结果均为0；
            cnt=1, 其他值的结果为0，求排除0之后的乘积为0处的返回结果
            cnt=0, 求得整个数组的积，遍历用除法获得结果
         */
    }
}