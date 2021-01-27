/**
 * @param {number} n
 * @return {number}
 */
var fib = function(n) {
    //带备忘录的递归解法（递归树的剪枝）--类似“迭代的动态规划解法”
    if (n < 1) { return 0;}
    if (n===1 || n===2) {return 1;}
    var pre=1, cur=1;
    var res = 0;
    for (let i=2; i<n; i++){
        res = pre + cur;
        // cur = res;
        // pre = cur; //顺序很关键，不能调换
        pre = cur;
        cur = res;
    }
    return res;
};