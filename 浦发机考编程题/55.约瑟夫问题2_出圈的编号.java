//温馨提示：需要自己处理输入输出
import java.util.*;

public class Main{

    public static int printOrder(int n, int m){
        //<>，泛型编程，使用引用类型
        // Queue<int> q = new LinkedList<>();
        Queue<Integer> q = new LinkedList<>();
        //创建模拟队列，并初始化
        for(int i=1; i<=n; i++){
            q.add(i); //在队尾添加元素
        }
        //遍历的下标visit, 遍历计数cnt or 遍历直到队列为空
        int visit = 1;
        while (!q.isEmpty()) {
            if (visit == m){
                System.out.println(q.remove());//获取队首元素并删除
                visit = 1;
            }
            else {
                //如果不是，将出列的元素添加至队尾
                q.add(q.remove());
                visit += 1;
            }
        }
        return 0;
    }

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // int n = sc.nextInt();
        // int m = sc.nextInt();
        // String[] temp = sc.next().split(",");
        String[] temp = sc.nextLine().split(" ");
        /* for (String s : temp){
            System.out.println(s);
        } */
        int n = Integer.parseInt(temp[0]);
        int m = Integer.parseInt(temp[1]);
        // int n = 5;
        // int m = 2;
        printOrder(n, m);
    }
}


// C++代码
/*
#include<iostream>
#include<queue>
using namespace std;

int main()
{
    int tot, outNum, nowNum = 1;
    queue<int> q;
    cin >> tot >> outNum;                        //读取数据
    for (int i = 1; i <= tot; i++)q.push(i);    //初始化队列
    while (!q.empty())                    //在队列不为空时继续模拟
    {
        if (nowNum == outNum)
        {
            cout << q.front() << " ";    //打印出局的人的编号
            q.pop();                    //出局
            nowNum = 1;                    //初始化现在的数字
        }
        else
        {
            nowNum++;
            q.push(q.front());            //排至队尾
            q.pop();
        }
    }
    cout << endl;
    return 0;
}
*/