
// 一道选择题，下面四个选项中，会导致死循环的是：
//正确答案为C，我错选了D
/*
c. for (int i=0; i<10; i--){}
d. for (int i=0; i>0; i++){}
*/

//test
public class Main{
    public static void main(String[] args){
        // 条件不满足，一次也不执行
        for (int i=0; i>0; i++){
            System.out.println("a" + i);
        }

        // 执行到i=2147400000 (理论上认为是死循环)
        /* for (int i=0; i>=0; i += 100000){
            System.out.println("b" + i);
        } */

        // 执行到i=-2147400000 (理论上认为是死循环)
        for (int i=0; i<10; i -= 100000){
            System.out.println("c" + i);
        }
    }
}