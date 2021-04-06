//题目描述：
// 输入一个整数，取出这个整数中的偶位上的数字组成一个新数并输出
// 例如输入123456，输出246 (偶数位是正着数的!!!)

import java.util.Scanner;

public class Main{

    public static int newNum(int n){
        // 计算整数的位数
        int count = 0, temp = n;
        while (temp != 0){
            count += 1;
            temp /= 10;
        }
        // 一位数则没有偶位上的数，返回0
        if (count < 2){
            return 0;
        }
        // System.out.println(count);
        // 创建一个刚刚够大的数组
        int[] nums = new int[count];
        temp = n;
        for (int i=count-1; i>-1; i--){
            nums[i] = temp % 10;
            temp /= 10; 
        }
        int res = 0;
        // 取偶位上的数，组成新的数
        for (int i=1; i<count; i+=2){
            res = res*10 + nums[i];
        }
        return res;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("input a interger: ");
        int n = sc.nextInt();
        // newNum(n);
        System.out.println(newNum(n));
    }
}