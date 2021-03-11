# 参考博客1：https://blog.csdn.net/idealcitier/article/details/82350418
# 参考博客2：https://jalenzhang.blog.csdn.net/article/details/77746375?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control

# python3
def getAllSubstring(strs):
    if len(strs)==0: return strs

    # 使用python语言作答，不允许使用切片操作 -- 
    # * 解决之道：自己定义一个slice方法
    def slice(strs, i, j):
        # [i, j) 左闭右开区间
        str = ''
        for i in range(i, j):
            str += strs[i]
        return str

    i = 0
    while i < len(strs):
        j = i+1
        while j < len(strs) + 1:
            # 切片：[i,j)，因此 j<len(strs)+1
            # print(strs[i:j])
            print(slice(strs, i, j))
            j += 1
        i += 1

getAllSubstring('abbc')