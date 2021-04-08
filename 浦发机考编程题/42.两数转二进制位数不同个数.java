/**
42.输入两个整数 M 和 N， 输出两个数转化为二进制后位数不同的个数。 
例如输入： 22 33 输出： 5
*/

import java.util.*;

public class Main{
    public static void main(String[] args){
        // 处理输入
        Scanner sc = new Scanner(System.in);
        String[] temp = sc.nextLine().split(" ");
        int m = Integer.parseInt(temp[0]);
        int n = Integer.parseInt(temp[1]);

        // -- 功能代码（直接实现）--
        int out = m^n; //先做异或，同0异1，统计out转为二进制后1的个数即可
        // 整数 转化为 二进制的字符串形式
        // String buff = Integer.toBinaryString(out);
        // char[] chars = buff.toCharArray();
        char[] chars = Integer.toBinaryString(out).toCharArray();
        int cnt = 0;
        for (char c : chars){
            if (c == '1'){
                cnt += 1;
            }
        }
        System.out.println(cnt);
    }
}