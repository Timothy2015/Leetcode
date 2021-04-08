// 题目描述
// []25.输入 n b, 找出 1-n 中被 b 整除的个数。 例： 输入 6 3 输出 2,(3 和 6)

import java.util.*;

public class Main{

    public static int dividedCnt(int n, int b){
        int cnt = 0;
        for (int i=1; i<=n; i++){
            if (b % i ==0){
                cnt += 1;
            }
        }
        return cnt;
    }

    public static void main(String[] args){
        // 处理输入
        Scanner sc = new Scanner(System.in);
        String[] temp = sc.nextLine().split(" ");
        int n = Integer.parseInt(temp[0]);
        int b = Integer.parseInt(temp[1]);

        // 调用功能函数
        System.out.println(dividedCnt(n, b));

    }
}