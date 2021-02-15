# https://leetcode-cn.com/problems/group-anagrams/

## 模式识别
# * 一旦需要根据特征进行归类，就应该利用散列表

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """        

        ## 一、排序
        # 1. 对每一个字符串元素排序，得到的结果作为哈希表的键
        # 2. 同一个键对应的值用list存储
        mp = collections.defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        return list(mp.values())

        ## 二、计数
        # - 新的特征：a:1,b:0,c:3,...,f:0（这是每一个键的模样）
        """
        mp = collections.defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希（键为不修改的变量）
            mp[tuple(counts)].append(st)
        
        return list(mp.values())
        """

        # 辅助函数：判断是否互为字母异位词
        # 法一
        def isAnagrams(s, t):
            if len(s) != len(t):
                return False
            a = set(s)
            for i in a:
                if s.count(i) != t.count(i):
                    return False
            return True
        # 法二
        def isAnagrams(s, t):
            if "".join(sorted(s)) != "".join(sorted(t)):
                return False
            return True
        
        # if len(strs)==1: return [strs]

        ## 先暴力求解：双重while循环 ---- 超出时间限制
        """
        i = 0
        res = []
        # 标记数组，已经添加为True, 否则为False
        flags = [0 for _ in range(len(strs))]

        # print(i, len(strs)-1)
        while i < len(strs):
            # 如果已经添加，则跳过
            if flags[i]: 
                # 必须执行:i的自增
                i += 1
                continue

            temp = [strs[i]]
            flags[i]  = 1
            
            j = i+1
            while j < len(strs):
                if flags[j]: 
                    # 必须执行:j的自增
                    j += 1
                    continue

                if isAnagrams(strs[i], strs[j]):
                    temp.append(strs[j])
                    flags[j] = 1
                j += 1
            res.append(temp)
            i += 1
        return res
        """
