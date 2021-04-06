/**
题目描述：
- 回文数相加的问题， 例如： 给出一个整数 n=2,输出回文数相加结果：1+121=？ 
- 输入整数 n=3 ， 输出回文数相加结果： 1+121+12321=？
 */

 import java.util.*;
 public class Main{
     // 1 --> 1
     // 2 --> 121
     // 3 --> 12321
     // 4 --> 1234321 //作为字符串处理比较简单
     // 递归公式：f(n) = f(n-1) + getNum(n) -- 可以用递归或迭代

     public static int getNum(int n){
         StringBuilder list = new StringBuilder();
         for(int i=1; i<=n; i++){
             list.append(i);
         }
         for(int i=n-1; i>=1; i--){
             list.append(i);
         }
         String s = list.toString();
        //  int res = s.parseInt();
         int res = Integer.parseInt(s);
         return res;
     }

     public static int getSum(int n){
         int ans = 0;
         for(int i=1; i<=n; i++){
             ans += getNum(i);
         }
         return ans;
     }

     public static void main(String[] args){
         //
         int n = 1;
         System.out.println(getSum(n));

     }
 }