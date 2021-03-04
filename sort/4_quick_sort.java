import java.util.*;

public class Solution {
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 将给定数组排序
     * @param arr int整型一维数组 待排序的数组
     * @return int整型一维数组
     */
    public int partition(int[] arr, int l, int r){
        int base = arr[l];
        while (l < r) {
            while (l < r && arr[r] >= base){
                r--;
            }
            arr[l] = arr[r];
            while (l < r && arr[l] <= base){
                l++;
            }
            arr[r] = arr[l];
        }
        arr[l] = base;
        return l;
        }
        
    public int[] quickSort(int[] arr, int l, int r){
        // base case 
        if (l < r){ 
            int mid = partition(arr, l, r);
            // quickSort递归，而不是patition递归
//             partition(arr, l, mid-1);
            quickSort(arr, l, mid-1);
//             partition(arr, mid+1, r);
            quickSort(arr, mid+1, r);
        }
        return arr;
    }
    
    public int[] MySort (int[] arr) {
        //冒泡排序
//         int[] nums = Arrays.copyOf(arr, arr.length);
//         for (int i=0; i<nums.length-1; i++){
//             boolean flag = true;
//             for (int j=0; j<nums.length-i-1; j++){
//                 if (nums[j] > nums[j+1]){
//                     int temp = nums[j];
//                     nums[j] = nums[j+1];
//                     nums[j+1] = temp;
//                     flag = false;
//                 }
//             }
//             if (flag){
//                 break;
//             }
//         }
//         return nums;
        // 快速排序
        return quickSort(arr, 0, arr.length-1);
    }
}