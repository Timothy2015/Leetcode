//题目描述：
// 输入一个整数，取出这个整数中的偶位上的数字组成一个新数并输出
// 例如输入123456，输出246 (偶数位是正着数的!!!)

import java.util.Scanner;

public class Main{

    public static int newNum(int n){
        // 整型转换为字符串处理
        String str = String.valueOf(n);
        // System.out.println(str);
        // System.out.println(GetType(str));
        // 字符串转换为字符数组
        String[] strs = new String[20]
        // System.out.println(strs[0]);

        if (strs.length < 2){return 0;}
        int res = 0;
        // arr.length 获取数组长度
        // str.length() 获取字符串长度
        for (int i=1; i<strs.length; i+=2){
            // System.out.println((int)strs[i]);
            // int num = Integer.valueOf(strs[i]);
            int num = Integer.parseInt(strs[i]);
            // res = res*10 + (int)strs[i];        
            res = res*10 + num;
            // System.out.println(res);
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