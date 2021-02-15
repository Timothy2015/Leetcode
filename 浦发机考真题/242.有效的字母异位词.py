# https://leetcode-cn.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ## 问题等价于：判断两个字符串有相同数量的字母
        # True: 'adbc' 'dbac'
        # True: 'anagram' 'nagaram'
        # True: 'aangram' 'ngaamra'
        # True: 'ram' 'mra' （完全错位时字母数量对应相等，也是True）

        ## 一、长度不等直接返回false, "剪枝"提高效率
        """
        if len(s) != len(t):
            return False

        sCounter = collections.Counter()
        tCounter = collections.Counter()

        # ---for循环---
        for c in s:
            sCounter[c] += 1
        for c in t:
            tCounter[c] += 1

        # ---while循环---
        # i = 0
        # while i < len(s):
        #     sCounter[s[i]] += 1
        #     tCounter[t[i]] += 1
        #     i += 1

        # if len(sCounter) > len(tCounter):
        for c in sCounter:
            if sCounter[c] != tCounter[c]:
                return False
        # else:
        #     for c in tCounter:
        #         if sCounter[c] != tCounter[c]:
        #             return False
        return True
        """

        ## 二：更加简洁的代码, 字符串的str.count()函数统计字符数量
        """
        if len(s) != len(t):
            return False
        a = set(s)
        for i in a:
            if s.count(i) != t.count(i):
                return False
        return True
        """

        ## 三：字符串排序之后再比较, python的sorted函数
        if len(s) != len(t):
            return False
        if "".join(sorted(s)) != "".join(sorted(t)):
            return False
        return True

        ## 下面的代码：由于对题意理解有偏差, 跳进去了，越写越复杂，且写不对
        """
        # 互为字母异位词，字符串长度相同
        if len(s) != len(t): return False
        # 双指针：i, j
        i = j = 0 
        while i < len(s):
            gap = 1 # 比较的间隔
            if s[i]==t[j]:
                i += 1
                j += 1
            elif i+gap >= len(s):
                # 遇到一对不等的字符，而后面没有字符了
                return False
            elif s[i+gap] == s[j+gap]:
                gap += 1
            elif s[i]==t[j+gap] and s[i+gap]==t[j]:
                i += 2
                j += 2
            else:
                return False
        return True
        """
