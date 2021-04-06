/**
题目描述：
- 找出正整数中偶数，并输出相加后的数，要用long
- 例如：输入5548，输出12
 */

import java.util.*;

public class Main{

    public static int sumOfEvenNums(int n){
        int res = 0;
        // 5548 --> 12
        int temp = 0; 
        while(n != 0){
            temp = n % 10;
            if (temp % 2 ==0){
                res += temp;
            }
            n = n / 10;
        }
        return res;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("input a positive integer:");
        int m = sc.nextInt();
        // int m = 5548;
        // m = 11000;
        // m = 2222;
        System.out.println(sumOfEvenNums(m));
    }
}