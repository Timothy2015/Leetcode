// Leetcode:
// https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/
// 牛客网：
// https://www.nowcoder.com/practice/554aa508dd5d4fefbf0f86e5fe953abd?tpId=188&tqId=38297&rp=1&ru=%2Factivity%2Foj&qru=%2Fta%2Fjob-code-high-week%2Fquestion-ranking&tab=answerKey

class Solution {
    public int maxSubArray(int[] nums) {
        // 贪心策略 or 动态规划
        // 状态转移方程
        // 为什么能想到看dp[i-1]的正负呢？ --- 其实是一种贪心策略（累积相抵后的正收益）
        int dp_i_1 = nums[0], dp_i_2 = nums[0]; //额外空间O(1)
        int res = nums[0];
        for (int i=1; i<nums.length; i++){
            dp_i_2 = Math.max(dp_i_1, 0) + nums[i]; //前面若是负收益，则不如不要
            res = Math.max(res, dp_i_2); //保存历史过程中的最大值
            dp_i_1 = dp_i_2;
        }
        return res;


        // 错误的思路2：没有理解到问题的关键，要看dp[i-1]的正负
        // 状态dp[i],到（包含）nums[i]的最大连续子数组的和
        // dp[i-1] --> dp[i], 如果nums[i]>0,dp[i] = dp[i-1]+nums[i]; 否则dp[i] = dp[i-1]
        // 最后返回dp数组的最大值，dp[i]的只与相邻状态有关
        /*
        int dp_i = nums[0], res = nums[0];
        for (int i=1; i<nums.length; i++){
            dp_i += Math.max(nums[i], 0); //状态转移方程
            res = Math.max(res, dp_i);
        }
        return res;
        */
        
        // 不要好高骛远！一心一意，踏踏实实为浦发备战！
        
        // 错误的思路1：双指针(这个思路有问题)
        /*
        int l = 0, r = 1;
        while (nums[l] < 0){
            l++;
            r = l + 1;
        }
        int max = nums[l], sum = nums[l];
        while (r < nums.length) {
            sum += nums[r];
            if (sum > max){
                max = sum;
            }
            r++;
        }
        while (l < nums.length){
            sum -= nums[l];
            if (sum > max){
                max = sum;
            }
            l++;
        }
        return max;
        */
    }
}