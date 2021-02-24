# https://leetcode-cn.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        if not A: return A
        ### 对每一行内的元素逆序反转（而不是逆序整个列表）
        def reverse(A):
            mid = len(A)//2
            if len(A) % 2 ==1 :
                l = mid 
                r = mid
            else:
                l = mid-1
                r = mid
            while l>=0 and r<=len(A)-1:
                ##### --------优化：在交换的时候互换0和1--------
                A[l],A[r] = 1-A[r], 1-A[l]
                # A[l],A[r] = A[r], A[l]
                l -= 1
                r += 1
        
        for i in range(len(A)):
            # 反转每一行内部的元素
            reverse(A[i])

            # 每个元素取反 —— 有没有特别快的方法？
            # map(func, [list])
            # A[i] = list(map(lambda x:1-x, A[i]))
            # 这里不需要按位取反，只需要对换0和1
            """
            # ~:按位取反，对二进制进行操作
            # A[i] = map(lambda x: int(~bin(x)), A[i])
            """            
        return A
