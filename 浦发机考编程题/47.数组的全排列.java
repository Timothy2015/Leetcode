// 题目描述
// * 给定数列a, 按全排列顺序打印数列

// leetcode-46.全排列（回溯算法）
// https://leetcode-cn.com/problems/permutations/

import java.util.*;

public class Main{
    
    // 全排列 - 回溯算法

     public static void backTrace(List<Integer> trace, List<List<Integer>> res, int first){
        // 满足要求的完整路径，添加进res
            if (first == trace.size()){
                res.add(new ArrayList(trace));
            }

            for( int i=first; i<trace.size(); i++){
                // 做出选择: 交换操作 + "fisr+1
                Collections.swap(trace, first, i);
                backTrace(trace, res, first + 1);
                // 撤销选择：交换操作
                Collections.swap(trace, first, i);
            }
        }

    public static List<List<Integer>> permute(int[] nums) {
        // 递归求解（回溯法）
        List<List<Integer>> res = new ArrayList<List<Integer>>();

        List<Integer> trace = new ArrayList<>();
        for (int num : nums){
            trace.add(num);
        }

        backTrace(trace, res, 0);
        return res;
    }

    public static void main(String[] args){
        // test
        // String s = "abc";
        int[] nums = {1, 2, 3};
        List<List<Integer>> ans = permute(nums);
        System.out.println(Arrays.toString(ans.toArray()));
    }
}