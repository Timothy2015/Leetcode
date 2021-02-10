class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        # 集合去重并升序排列
        arr1 = sorted([x for x in set(nums1)])
        arr2 = sorted([y for y in set(nums2)])
        ans = []
        # 双指针遍历，时间复杂度O(n+m)
        i = 0; j = 0
        while i<len(arr1) and j<len(arr2):
            print(i,j)
            if arr1[i] == arr2[j]:
                ans.append(arr1[i])
                i += 1
                j += 1
            elif arr1[i] < arr2[j]:
                i += 1
                
            else:
                j += 1
        return ans
        """
        
        s1 = set(nums1)
        s2 = set(nums2)
        return [x for x in s1.intersection(s2)]






# javascript代码
"""
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    // 数组去重并升序排列
    arr1 = Array.from(new Set(nums1)).sort((a,b)=>a-b);
    arr2 = Array.from(new Set(nums2)).sort((a,b)=>a-b);
    // 双指针
    var i = 0;
    var j = 0;
    var res = [];
    while (i<arr1.length && j<arr2.length){
        if (arr1[i]===arr2[j]){
            res.push(arr1[i]);
            i++;
            j++;
        }
        if (arr1[i] < arr2[j]){
            i++;
        }
        if (arr1[i] > arr2[j]){
            j++;
        }
    }  
    return res;
};
"""