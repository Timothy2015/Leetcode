# 题目描述：
# * 给出某年某月某日，求出该日期是该年的第几天

# CSDN题解:https://blog.csdn.net/qq_43328781/article/details/85328913?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&dist_request_id=1328665.10290.16159875586415497&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control

"""年份月数的基础常识"""
# 1. 平年一年365天，闰年一年366天，闰年多出的一天，多在2月；
# 2. 平年1-12月的天数
#   [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 3. 闰年1-12月的天数
#   [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# 4. 每年的7-8月均为大月，大月31天，一月大，二月小，三月大，四月小，如此交替，小月30天
# 5. 二月平年为28天，闰年为29天
"""
一月大，二月小，三月大，四月小……
七八月例外，均为大月
大月31天，小月30天
二月最特殊，平年28天，闰年29天
"""

def day_of_year(year, month, day):
    # 定义一个枚举每月天数的列表
    days = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 31, 30]
    # days_norm = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 31, 30]
    # days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 31, 30, 31, 30]

    # 参数year: 判断是否是闰年
    # 整百年能被400整除，非整百年能被4整除
    if (year%4==0 and year%100!=0) or year%400==0:
      # 闰年二月的天数为29
      days[1] = 29
    
    # 参数month: 累积统计天数(注意要少算一个月，当月的天数为传入的day)
    res = 0
    for i in range(month-1):
      res += days[i]
    
    # 加上当月的天数
    res += day

    return res

# test
print(day_of_year(2001, 3, 1)) # 60
print(day_of_year(2000, 3, 1)) # 61
print(day_of_year(2019, 5, 10)) # 130

      

      








# 下面是C代码
"""
int day_of_year(year, month, day){
  
  int sum = 0,i;
    int a[12] = {31,28,31,30,31,30,31,31,30,31,30,31};
    int b[12] = {31,29,31,30,31,30,31,31,30,31,30,31}; 
    
    if ( year%4==0&&year%100!=0||year%400==0) { 
        for (i = 0; i < month - 1; i++) {
            sum += b[i];
        }
    }else{
        for (i = 0; i < month - 1; i++) {
            sum += a[i]; 
        }
    }
    
    sum += day;  
    return sum;
}
"""