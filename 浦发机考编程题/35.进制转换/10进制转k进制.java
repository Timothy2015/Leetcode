
import java.util.*;

public class Main{

    public static String getKNumber(int n, int k){
        // k = 2,8,16来理解，尤其是16进制，需要特殊处理
        int m = n;

        // 先判断位数
        int cnt = 0;
        while(m != 0){
            cnt += 1;
            m /= k;
        }
        // System.out.println(cnt);

        //创建大小刚刚好的数组
        int[] nums = new int[cnt];
        String str = "";
        for(int i=cnt-1; i>=0; i--){
            // 除k取余法
            nums[i] = n % k;
            n /= k;
            // 十六进制：10~15, A~F
            if (nums[i] >= 10 && nums[i] <=15){
                char temp = (char)('A' + nums[i] - 10);
                str = temp + str;
            }
            else{
                str = nums[i] + str;
            }
        }

        // int res = Integer.parseInt(Arrays.toString(nums));
        // int res = Integer.parseInt(str);
        // return res;

        return str;


        // 练习Arraylist和StringBuilder的使用，可以按下面的方法写
        /*
        ArrayList<Integer> list = new ArrayList();
        // 除k取余法
        while( m != 0){
            list.add(m % k);
            m /= k;
        }

        // 倒序过来，拼接成结果（list不能用下标遍历，所以转为array）
        Object[] arr = list.toArray();
        // int[] arr = list.toArray();
        StringBuilder res = new StringBuilder();
        for (int i=arr.length-1; i>=0; i--){
            res.append(arr[i]);
        }
        return res.toString();
        */
    }

    public static void main(String[] args){
        // test
        int n = 171;
        int k = 16;
        System.out.println(getKNumber(n, k));

    }
}