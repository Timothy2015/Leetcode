// 输入一个正整数，判断是否为素数
// 素数：除了1和它本身以外，没有被其他的数可以被整除（最小的素数为2）

import java.util.Scanner;

public class Main{
    
    // isPrime()
    public static boolean isPrime(int n){
        // 为什么只需要穷举到sqrt(n)+1?
        // 因为：可以数学证明 https://www.zhihu.com/question/21808179
        if (n < 2){return false;} // 最小的素数为2
        if (n==2){return true;}
        for (int i=2; i<Math.sqrt(n)+1; i++){
            if (n % i == 0){
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        System.out.println("input a interger: ");
        int n = sc.nextInt();
        // 只需要：从1穷举到sqrt(n)+1（可以数学上严格证明）
        System.out.println("result: " + isPrime(n));
    }
}