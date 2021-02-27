# https://leetcode-cn.com/problems/sort-an-array/submissions/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 归并排序

        # 关键的归并操作
        def merge(left, right):
            res = []
            while left and right:
                if left[0] < right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            while left:
                res.append(left.pop(0))
            while right:
                res.append(right.pop(0))
            return res

        # 两段两段地递归划分数组，直到每组只包含一个元素
        def mergeSort(nums):
            ## base case
            if len(nums) < 2:
                # 长度为1，不再划分，返回自身（一定要返回）
                return nums
            
            mid = len(nums) // 2
            left = nums[0:mid]
            right = nums[mid:]
            return merge(mergeSort(left), mergeSort(right))
        
        return mergeSort(nums)


       
       