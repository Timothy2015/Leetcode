// Leetcode的第一题
// https://leetcode-cn.com/problems/two-sum/

import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] res = new int[2];
        // 需要熟练掌握java版哈希表的使用
        Map<String, Integer> mp = new HashMap<String, Integer>();
        for (int i=0; i<nums.length; i++){
            // containsKey(Object key) 是否存在特定的key
            if (mp.containsKey(String.valueOf(target - nums[i]))){
                res[0] = i;
                res[1] = mp.get(String.valueOf(target - nums[i]));
                break;
            }
            // mp[nums[i]] = i;
            mp.put(String.valueOf(nums[i]), i);
        }
        return res;
    }
}