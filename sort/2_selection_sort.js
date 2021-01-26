//选择排序（selection_sort）的思路
/* 选择排序的步骤：
 * 1. 首先在未排序的序列中，找到最小（或最大）的元素，将它放在第一个位置；
 * 2. 在剩下的元素列表中，继续寻找最小的元素，将它放在剩下元素序列的第一个位置；
 * 3. 重复第二步，直到最终排序完成
 * 
 * 关键提示：需要获得最小元素的位置索引，方便执行交换操作。
 */

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    //选择排序
    // var res = [];
    for (let j=0; j<nums.length-1; j++){
        var minIndex = j;
        for (let i=j+1; i<nums.length; i++){
            if (nums[minIndex] > nums[i]){
                minIndex = i;
            }
        }
        // res.push(min);
        // 需要用到数组的索引信息
        [nums[j], nums[minIndex]] = [nums[minIndex], nums[j]];
    }
    // return res;
    return nums;
};