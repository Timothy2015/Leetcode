//题目描述：
// 1 + 2/3 + 3/5 + 4/7 + ......
import java.util.*;

public class Main{

    public static double getSum(double n){
        double sum = 0;
        for (double i=1; i<=n; i++){
            sum += 1.0 * (i / (2*i-1));
            // System.out.println(i/(2*i-1) + i%(2*i-1));
        }
        return sum;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("input a integer: ");
        double n = sc.nextDouble();
        System.out.println("1 + 2/3 + 3/5 + ... + n/(2*n-1) = ");
        // 分数求和,必须全部使用double类型，使用int得到的结果总为1
        // int类型：2/3=0; 3/5=0;4/7=0
        // 输入值用double，循环变量用double，结果也用double
        System.out.println(getSum(n));
    }
}