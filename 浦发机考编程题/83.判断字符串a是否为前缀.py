# 问题描述：
# 83、判断字符串a是否是字符串序列中单词的前缀，是则输出输出单词（换行输出）

strings = 'Blessed are all who fear the LORD, who walk in obedience to him.'
prefix = 'a'

def findPrefix(strings, prefix):
    strs = strings.split(' ')
    # print(strs_arr)
    for str in strs:
        # 如果长度小于prefix，跳过
        if len(str) < len(prefix):
            continue
        i = 0
        while i < len(prefix):
            if str[i] != prefix[i]:
                break
            i += 1
        if i == len(prefix):
            print(str)

findPrefix(strings, prefix)