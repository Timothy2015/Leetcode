# https://leetcode-cn.com/problems/degree-of-an-array/

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## 使用字典，每个val为一个list/三元数组，分别保存count, left, right
        # key:val[0,1,2]
        # count: 出现的次数
        # left: 第一次出现的位置
        # right: 最后一次出现的位置
        mp = collections.defaultdict(list)
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]][0] += 1
                mp[nums[i]][2] = i
            else:
                mp[nums[i]] = [1, i, i]
                # mp[nums[i]].append(1)
                # mp[nums[i]].append(i)
                # mp[nums[i]].append(i)
        # for k,v in mp.items():
            # print(k,v)

        maxCount = 0; minLen = 50001
        for v in mp.values():
            if maxCount < v[0]:
                maxCount = v[0]
                # 最大值更新了，长度必须更新
                minLen = v[2]-v[1]+1
            if maxCount == v[0]:
                # 相同的最大值，再比较长度
                if minLen > v[2]-v[1]+1:
                    minLen = v[2]-v[1]+1
        return minLen

        ## 低配版的解法：遍历次数太多，效率低下，如何改进？---设计更加合理的数据结构
        """
        # 计数器
        c = collections.Counter()
        for i in nums:
            c[i] += 1
        degree = c.most_common(1)[0][1]
        target = []
        for k,v in c.items():
            if v==degree:
                target.append(k)
        # 双指针：left, right遍历数组
        min_len = 50001
        for t in target:
            left = 0; right = len(nums)-1
            while nums[left] != t:
                left += 1
            while nums[right] != t:
                right -= 1
            # print(left, right)
            if right - left + 1 < min_len:
                min_len = right - left + 1
        return min_len
        """

        ###---Couter()基础---###
        # 打印所含的每一个元素，包含重复的元素
        """
        for k in c.elements():
            print(k)
        """
        # 从dict继承的items()
        """
        for k,v in c.items():
            print(k,v)
        """
        # most_common(指定一个参数n，列出前n个元素，不指定参数，则列出所有)
        """
        print(c.most_common(1)) # [(1,2)]
        print(c.most_common(1)[0][1]) # 取出最大值2
        """
