# 判断一个字符串中数字， 大小写字母、 空格
# 以及特殊字符的数量并输出

print('input a string:')
str = input()

def countNumber(str):
    num = char = nbsp = special = 0
    for i in range(len(str)):
        # 数字
        # nums = ['0','1','2','3','4','5','6','7','8','9']
        # if str[i] in nums:
        #     num += 1
        ## 字符串形式的'0','1',...,'9'也可以直接比较
        if str[i]>='0' and str[i]<'9':
            num += 1
        # 大小写字母
        # elif (str[i]>='a' and str[i]<='z') or (str[i]>='A' and str[i]<='Z') :
        elif str[i].lower() >= 'a' and str[i].lower() <= 'z':
            char += 1
        # 空格
        elif str[i] == ' ':
            nbsp += 1
        else:
        # 特殊字符 (其他字符均视为特殊字符)
            special += 1
    return [num, char, nbsp, special]

res = countNumber(str)
print("num: ", res[0], " char: ", res[1], " nbsp: ", res[2], " special: ", res[3])
