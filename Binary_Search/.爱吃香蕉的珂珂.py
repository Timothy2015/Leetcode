# https://leetcode-cn.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # 二分查找 - case2 - leftBound
        # 提示得知：10^9>=H>=piles.length, K一定不大于数组的最大值

        def canFinish(piles, mid, H):
            time = 0
            for n in piles:
                time += n//mid # 正好H能吃满的次数
                time += 1 if n%mid > 0 else 0 # 剩余不足的，还要吃一次
            return time <= H

        """1 =< H <= max(piles) 连续空间的搜索问题，二分查找左侧边界"""
        ###--------------缩小区间技巧，无关二分查找本身------------------------------
        # 1 小时数等于数组长度
        if H==len(piles): return max(piles)
        # 2 这个技巧有点难想，另外不具有普遍性
        sump = sum(piles)
        left = (sump - 1) // H + 1
        right = min(max(piles), sump // (H - len(piles)))
        # left = 1
        # right = max(piles)
        ###--------------------------------------------
        while left <= right:
            mid = left + (right-left)//2
            # 这里以mid能吃完和不能吃完两种情况
            if canFinish(piles, mid, H):
                # 寻找左侧边界，right缩小
                right = mid - 1
            else:
                # mid太小不能吃完，增大
                left = mid + 1
        # 一定能找到，省略了一些边界处理
        return left



"""用时最短的代码"""
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        def dfs(m):
            return sum((p - 1) // m + 1 for p in piles) <= H

        n = len(piles)
        maxp = max(piles)
        if H == n: return maxp
        sump = sum(piles)
        left = (sump - 1) // H + 1
        right = min(maxp, sump // (H - n))
        while left < right:
            mid = (left + right) >> 1
            if dfs(mid):
                right = mid
            else:
                left = mid + 1
        return left