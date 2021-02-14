# 题目描述：
# * 判断闰年：输出从1990年到2010年之间的闰年
def isLeapYear(year):
    if year < 0:
        print("年份不能为负数，请重新输入!")
        return

    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

for i in range(1900,2011):
    if isLeapYear(i):
        print(i)