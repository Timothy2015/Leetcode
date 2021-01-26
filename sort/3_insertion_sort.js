/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArray = function(nums) {
    //插入排序
    /* 有时候出现的整体后移：分解为一步步的交换操作 */
    for (let i=1; i<nums.length; i++){
        for (let j=i; j>0; j--){
            if (nums[j] < nums[j-1]){
                [nums[j], nums[j-1]] = [nums[j-1], nums[j]];
            }
            else{
                // continue; //已经找到何时位置，提前跳出当次循环
                break;
            }
        }
    }
    return nums;
};
