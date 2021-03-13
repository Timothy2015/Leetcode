// 字符串移除奇数位置上的字符

import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("input a string: ");
        String str = sc.nextLine();
        System.out.println(omitOddBit(str));
    }

    public static String omitOddBit(String str){
        //思路1: StringBuilder, 不可行
        // StringBuilder s = new StringBuilder(1024);

        //思路2: String转换为Char[]
        char[] cs = str.toCharArray();
        String new_str = "";
        for (int i=1; i<cs.length; i+=2){
            new_str += cs[i];
        }
        return new_str;
    }
}