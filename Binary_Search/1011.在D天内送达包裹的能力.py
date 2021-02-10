# https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        # 二分查找- 寻找左侧边界
        def canArrive(weights, C, D):
            sum = 0
            count = 0
            for i in weights:
                # 单个商品重要要大于i
                # if i > C: return 0 # 测试用例[1,2,3,1,1] 4
                if sum + i <= C:
                    sum += i
                else:
                    count += 1
                    sum = i
            # 最后一个i的补丁
            count += 1
            return count<=D

        # C的取值范围：1<=C<=sum(weights)
        # left = 1
        """增大left: C一定不小于单个商品重量的最大值"""
        left = max(weights)
        # right = sum(weights)
        """缩小right: 下面的right值是一个一定可行的值，但不是最小值"""
        right = left * len(weights) // D # 这个值比sum(weights)小多了
        while left <= right:
            mid = left + (right-left)//2
            if canArrive(weights, mid, D):
                # mid可以送达，缩小范围
                right = mid - 1
            else:
                left = mid + 1
        # 应是一定有解
        return left



