/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {

    const hashMap = new Map();
    
    return function(...args) {
        var hash = JSON.stringify(args);
        if (hashMap.has(hash)) {
            return hashMap.get(hash);
        }
        var res = fn(...args);
        hashMap.set(hash, res);
        return res;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */