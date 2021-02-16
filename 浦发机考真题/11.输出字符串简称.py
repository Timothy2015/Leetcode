# 例如字符串是“end of file”, 输出“EOF”

def abbreviation(s):
    if s=='': return ''
    # 分割成一个个单词
    sList = s.split(' ')
    res = []
    for word in sList:
        abr = word[0].upper()
        res.append(abr)
    return ''.join(res)
    
print(abbreviation('end of file'))
print(abbreviation(''))
print(abbreviation('end'))

