//约瑟夫问题：求最后幸存者的编号
// 牛客地址：https://www.nowcoder.com/questionTerminal/67741e15f1404e9fb26fd8192f02a870


/**
递归公式 -- live的编号必须从0开始，递归公式才成立，最后输出打印时整体加1即可
n = 1, live = 0
n = n, live = (live + m) / i, i=2......n
*/

import java.util.*;

public class Main{
    public static void main(String[] args){
        //处理输入
        Scanner sc = new Scanner(System.in);
        String[] temp = sc.nextLine().split(" ");
        // String to Int
        int n = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);
        
        // 递推公式求解（注意：live必须从0开始编号，这样递推公式才成立）
        //              末尾打印的时候，再整体加1即可
        int live = 0;
        for(int i=2; i<=n; i++){
            live = (live + m) % i;
        }
        System.out.print(live+1);
    }
}