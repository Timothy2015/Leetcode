/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    //解法一：迭代的动态规划（DP）方法
    // 创建长度为amount+1的dp数组，初始化为amount+1（等价于INF）,保存中间结果
    var dp = [];
    for (let i=0; i<amount+1; i++){dp.push(amount+1);}
    // base case 
    dp[0] = 0;
    // 迭代求解：dp[i] = 1 + min(dp[i-k0],...,dp[i-kj]},coins长度为j+1
    for (let j=1; j<amount+1; j++){
        coins.forEach(coin => {
            // console.log(coin);
            if (j - coin < 0) {}
            else{
                dp[j] = Math.min(dp[j], 1 + dp[j-coin]);
            }
        })
    }
    return (dp[amount] === amount+1) ? -1 : dp[amount];
};


/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    //解法二：带备忘录的递归解法
    // 创建Demo
    var Demo = {};

    function dp(n) {
        //base case
        if (n===0) {return 0;}
        if (n<0) {return -1;}
        //查找备忘录，避免重复计算
        if (n in Demo) return Demo[n]; //字典的使用不熟练

        var res = amount + 1;
        coins.forEach(coin => {
            // console.log(coin);
            subProblem = dp(n-coin)
            if (subProblem < 0) {}
            else{
                res = Math.min(res, 1 + dp(n-coin));
            }
        })
        //添加到备忘录
        Demo[n] = (res === amount+1)? -1 : res;
        return Demo[n];
    }    
    return dp(amount);
};