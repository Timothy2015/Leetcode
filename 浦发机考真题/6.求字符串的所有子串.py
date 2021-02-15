# 参考博客1：https://blog.csdn.net/idealcitier/article/details/82350418
# 参考博客2：https://jalenzhang.blog.csdn.net/article/details/77746375?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control

# python3
def getAllSubstring(s):
    if len(s)==0: return s

    i = 0
    while i < len(s):
        j = i+1
        while j < len(s) + 1:
            # 切片：[i,j)，因此 j<len(s)+1
            print(s[i:j])
            j += 1
        i += 1

getAllSubstring('abbc')