# partition子函数是关键，剩余的逻辑就是二叉树的前序遍历

"""递归提速的技巧：
* 递归的主体尽量简单，降低递归栈的深度
"""


## 写法二：patition操作作为单独的函数，递归逻辑写在quickSort里面
# 问题：
# * leetcode上可以通过
# * 在牛客上超时（貌似牛客对python的时间限制为2秒，只有调用库函数可以通过）

class Solution:
    def MySort(self, arr):
        # 分解子操作
        def parititon(arr ,low, high):
            ## 2021.2.27 目前发现最优美的partition写法（对称美） 
            # * 注意：这个方法不适用于随机快排，需要固定base为第一个数
            base = arr[low]
            while low < high:
                while low<high and arr[high]>=base:
                    high -= 1
                # 找到比base小的，换到左边来
                arr[low] = arr[high]
                while low<high and arr[low]<=base:
                    low += 1
                arr[high] = arr[low]
            arr[low] = base
            return low
        
        def quickSort(arr, low, high):
            if low > high: return 
            mid = parititon(arr, low, high)
            quickSort(arr, low, mid-1)
            quickSort(arr, mid+1, high)
        
        quickSort(arr, 0, len(arr)-1)
        return arr


## 写法一：把递归放在patition操作里面
# 问题：逻辑没错，但是运行超时 （在牛客+leetcode上超时）

class Solution:
    def MySort(self , arr ):
        # quick sort
        def partition(start, end):
            # base case
            if start > end: return
            # 取第一个数为基准
            pivot = start
            idx = pivot + 1
            for i in range(start+1, end+1):
                if arr[i] < arr[pivot]:
                    # 关键操作：pivot何时交换？？？那这里交换什么
                    arr[i], arr[idx] = arr[idx], arr[i]
                    idx += 1
            # 最后才交换arr[pivot]，保证左边都小于arr[pivot]，右边都大于arr[piovt]
            arr[pivot], arr[idx-1] = arr[idx-1], arr[pivot]
            pivot = idx-1
            
            partition(start, pivot-1)
            partition(pivot+1, end)
            
        partition(0, len(arr)-1)
        return arr