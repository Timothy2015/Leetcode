# https://leetcode-cn.com/problems/jump-game/

# labuladong题解：https://labuladong.gitbook.io/algo/dong-tai-gui-hua-xi-lie/tan-xin-lei-xing-wen-ti/tiao-yue-you-xi

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 贪心策略：能跳到的最远距离 fastest >= len(nums)
        n = len(nums)
        # 下标从0开始，跳跃的距离也从0开始
        fastest = 0
        ## 为什么i不能取到最后一个数？？
        # 1.长度为1时，已经到达最后一个下标，不需要考虑
        # 2.长度超过1时，同理，最后一个下标是不需要考虑的i=n-1，一定可达
        for i in range(n-1):
            # i+nums[i], 已达到当前位置，可跳跃的最大距离
            fastest = max(fastest, i + nums[i])
            ## 什么时候跳不下去呢？
            # 遇到了0且没有跨过去
            if fastest <= i:
                return False
        return fastest >= n-1