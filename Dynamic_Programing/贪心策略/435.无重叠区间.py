# https://leetcode-cn.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ## 贪心策略之区间问题

        if not intervals: return 0

        # 1.每个区间为[start, end]，按照end将区间升序排序
        intervals.sort(key = lambda x:x[1])
        
        # 2.需要移除的区间，即重叠的区间
        # * 这里与count统计最大不重叠区间数，本质相同
        remove = 0
        # 找到最小的end
        min_end = intervals[0][1]
        # 排序后的第一个区间，end最小肯定保留，for从1开始
        for i in range(1, len(intervals)):
            start = intervals[i][0]
            if start < min_end:
                remove += 1
            else:
                # 不重叠则保留，更新min_end
                min_end = intervals[i][1]
        return remove





