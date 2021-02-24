# https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ## 贪心策略之区间问题
        # 注意：不同问题的边界定义不同，处理略有差异
        # * 边界特殊：这里若有一侧边界相等，属于重叠区间
        # * 因为，最小剪数为“边界相等算重叠”条件下的最大不重叠区间数

        if not points: return 0

        # 1.[start, end], 按照end原地排序
        points.sort(key = lambda x:x[1])

        # 2.找到最小的end
        min_end = points[0][1]
        # 第一个肯定保留
        count = 1
        for point in points:
            start = point[0]
            # 注意：边界相等算重叠
            if start > min_end:
                count += 1
                min_end = point[1]
        return count