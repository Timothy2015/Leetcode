
import java.util.*;

public class Main{

    public static int getDNumber(String s, int k){
        // k = 2, 8, 16 来理解
        // 十六进制：1，2，3，......,9,A,B,C,D,E,F
        char[] cs = s.toCharArray();
        int len = cs.length;
        int res = 0;
        for (int i=len-1; i>=0; i--){
            // int n = Integer.parseInt(cs[i]);
            int n;
            if (cs[i] >= 'A' && cs[i] <= 'Z'){
                n = cs[i] - 'A' + 10;
            }
            else{
                // char to int : '9' --> 9
                // char的封装类 Character 的getNumericValue((int)char)
                // int n = Character.getNumericValue((int)cs[i]);

                /* the best way: '9'-->9 */
                n = cs[i] - '0';
            }

            if (n > k){
                // 输入有误！有位上的数字大于k
                System.out.println("wrong input!");
                return -1;
            }
            res += n * Math.pow(k, len-1-i);
        }
        return res;
    }

    // 1010 = 1*2^3 + 1*2^1
    public static void main(String[] args){
        // 处理输入
        Scanner sc = new Scanner(System.in);
        System.out.println("Input a string:");
        String s = sc.nextLine();
        System.out.println("input the value of k:");
        int k = sc.nextInt();

        // 调用主函数
        System.out.println(getDNumber(s, k));
    }
}