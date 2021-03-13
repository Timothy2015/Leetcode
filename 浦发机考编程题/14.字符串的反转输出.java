// 字符串的反转输出

import java.util.*;

public class Main{

    public static String reverseStr(String str){
        String new_str = "";
        //String转换为char[]数组来处理
        char[] cs = str.toCharArray();
        for (int i=cs.length-1; i>-1; i--){
            new_str += cs[i];
        }
        return new_str;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("input a string: ");
        String str = sc.nextLine();
        System.out.println(reverseStr(str));
    }
}