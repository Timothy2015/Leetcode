// 判断闰年
// 输出1990到2010之间的闰年

// 闰年：
// 1.整百年，能被400整除
// 2.非整百年，能被4整除（+ 如何判断为非整百年，不能被100整除）

public class Main{

    // static方法，即类方法（类方法不能调用非类方法）
    public static boolean isLeapYear(int n){
        if (n < 0){return false;}
        if (n % 400 == 0 || (n % 4 ==0 && n % 100 != 0)){
            return true;
        }
        else{
            return false;
        }
    }

    public static void main(String[] args){
        for (int i=1990; i<=2010; i++){
            if (isLeapYear(i)){
                // System.out.println(i);
        }
        }
        // java输出2^n
        // int n = 10;
        // System.out.println(2^3);//错误的表示，这是位运算
        // System.out.println(Math.pow(2,n)); //这是2的3次方，乘方的运算
        // System.out.println(Math.sqrt(2)); // 1.41
    }
}