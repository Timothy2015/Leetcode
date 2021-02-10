class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 1.先排序
        # sorted(nums) # 新建一个列表
        nums.sort() # 只对列表排序，原地操作
        # 2.双指针遍历操作
        # * 固定最长边，即末尾的元素nums[i]
        # * 双指针l=0,r=i-1开始遍历
        ans = 0
        # for i in range(len(nums)-1, -1, -1):
        for i in range(len(nums)-1, 1, -1): # 最长边从第3个元素起
            l = 0; r = i-1
            # while循环，把含当前最长边的有效组合遍历完全
            while l!=r:            
                if nums[l]+nums[r] > nums[i]:
                    ans += r-l
                    r -= 1
                else:
                    l += 1
        return ans
