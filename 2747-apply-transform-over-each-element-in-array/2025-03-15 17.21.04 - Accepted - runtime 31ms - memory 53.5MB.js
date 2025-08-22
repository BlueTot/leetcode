/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    var output = [];
    for (let i = 0; i < arr.length; i++) {
        output.push(fn(arr[i], i));
    }
    return output;
};