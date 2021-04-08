/* 
27.输入一个数 n， 计算 1 （1 2） （1 2 3） ..... （1 2 ... n）
    关键：正确理解题意—— 1 + （1+2）+ (1+2+3) + ...... + (1+2+...+n)
*/

import java.util.*;

public class Main{

    public static int getSum(int n){
        // 法一：双重for循环暴力求解

        // 法二：数学公式 - 等差数列求和
        // adder(n) = (1+n)n/2
        int sum = 0;
        for (int i=1; i<=n; i++){
            int adder = i*(1+i)/2;
            sum += adder;
        }
        return sum;        
    }

    public static void main(String[] args){
        // 处理输入
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        //调用功能函数
        System.out.println(getSum(n));
    }
}