# https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 升序数组：二分查找
        # 双指针：一个定位最小元素，一个定位最大元素
        i = 0
        j = len(numbers) -1 
        while i!=j: # 不等于，因为不可以重复使用相同元素
            if numbers[i] + numbers[j] == target:
                # 下标从1开始奇数
                # return [i,j]
                return [i+1, j+1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return []

"""最快的解题方案：哈希表"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idxDict = dict()
        for idx, num in enumerate(numbers):
            if target - num in idxDict:
                return [idxDict[target - num]+1, idx+1]
            # 添加 val:idx 的键值对
            idxDict[num] = idx