//-----------冒泡排序-js实现---------------------
/* 需要注意的点：
 *  1.终止条件：最多n-1躺，for循环实现
 *  2.从右端开始比较，即从数组的后面开始往前比较
 *  3.处理特殊情况（一些边界测试用例）
 */
function bubbleSort (arr) { 
    //关键问题：如何确定终止条件？--最多冒泡几次呢，n-1次，排好了前n-1个数，第n个数自动拍好了
    for (let end=arr.length-1; end>0; end--){
        var flag = true;
        //一次冒泡，把一个数放在正确的位置，最多n-1躺
        for (let i=0; i<arr.length-1; i++){
            if (arr[i]>arr[i+1]){
                [arr[i],arr[i+1]] = [arr[i+1], arr[i]];
                flag = false;
            }
        }
        if (falg === ture){
            break;
        }
    }
    return(arr);
}
//TDD:测试驱动开发
arr = [1,3,2]
arr = bubbleSort(arr)
console.log(arr);

arr2=[];
arr2 = bubbleSort(arr2);
console.log(arr2);

arr3=[3];
arr3 = bubbleSort(arr3);
console.log(arr3);

//---------上面的代码在leetcode-排序数组一题提交了，运行效率低下，如何优化？---
/* 思路一：上面是固定循环n-1次，如果提前排好了序，提交终止循环 
 * 备注：因为该算法本身时间复杂度高，换排序思想更加重要，上面的思路一的改进不能扭转劣势。
*/