# https://leetcode-cn.com/problems/sorted-merge-lcci/

class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        ## 思路三：逆向双指针 时间复杂度O(n+m), 空间复杂度O(1)
        """ m代表数组A的长度，而不是len(A)"""
        p = m-1; q = n-1
        last = p + q + 1
        while p >= 0 and q >= 0:
        # while last >= 0:
            print(p, q)
            if A[p] > B[q]:
                A[last] = A[p]
                p -= 1
            else:
                A[last] = B[q]
                q -= 1
            last -= 1
        # B没处理完, 剩余的是最小的元素
        while q>=0:
            A[last] = B[q]
            q -= 1
            last -= 1
        # A没处理完，因在A上原地修改，无需处理，排序已完成

        ## 思路二：正向双指针 时间复杂度O(n+m), 空间复杂度O(n+m) -- 一个临时的中间链表
        ## 思路一：原地排序，将B并入A中 - 插入排序 (操作复杂，不可行)



