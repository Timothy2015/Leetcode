// 
import java.util.Scanner;

public class Main{

    public static int[] num2Arr(int n){
        int count = 0, temp = n;
        while (temp!=0){
            count += 1;
            temp /= 10;
        }
        int[] nums = new int[count];
        temp = n;
        // for (int i=count-1; i>-1; i--){
        // 因为下面需要使用正序的下标，所有这里倒着存放
        for (int i=0; i<count; i++){
            nums[i] = temp % 10;
            temp /= 10;
        }
        return nums;
    }

    public static long arr2Num(int[] arr){
        long res = 0;
        for (int i=arr.length-1; i>-1; i--){
            res = res*10 + arr[i];
        }
        return res;
    }

    public static long bigNumsMuitiply(int n1, int n2){
        // 特殊情况的处理
        if (n1==0 || n2==0){return 0;}

        // 将两个大数转为数组
        int[] nums1 = num2Arr(n1);
        int[] nums2 = num2Arr(n2);
        // 两个n和m位的数相乘，最多得到n+m位的数
        int[] res = new int[nums1.length + nums2.length];
        // 先不管进位，求得的值在对应位置加和
        for (int i=0; i<nums1.length; i++){
            for (int j=0; j<nums2.length; j++){
                //res的最高位先空着
                res[i+j] += nums1[i] * nums2[j];
            }
        }
        // 处理进位
        for (int k=0; k<res.length-1; k++){
            // int carry = 0;
            if (res[k] > 10){
                // 先进位，再取模
                res[k+1] += res[k] / 10;
                res[k] %= 10;
                // carry = res[k] / 10;
                // res[k+1] += carry;

                // 需要到前面执行
                // res[k+1] += res[k] / 10;
            }
        }
        // 数组转换位数，返回
        return arr2Num(res);
    }

    public static void main(String[] args){
        // Scanner sc = new Scanner();
        Scanner sc = new Scanner(System.in); //需要传入参数System.in
        System.out.println("input two nums: ");
        int n1 = sc.nextInt();
        int n2 = sc.nextInt();
        // int的最大数：2 147 483 647
        // int res: 2 000 000 000 * 2 000 000 000 = -16515007200 (产生溢出)
        // long res: 2 000 000 0000 * 2 000 000 000 = 4 000000 0000000 000000
        long res = bigNumsMuitiply(n1, n2);
        System.out.println(res);        
    }
}