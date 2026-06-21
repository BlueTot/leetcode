/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var res = init;
    for (const num of nums) {
        res = fn(res, num);
    }
    return res;
};