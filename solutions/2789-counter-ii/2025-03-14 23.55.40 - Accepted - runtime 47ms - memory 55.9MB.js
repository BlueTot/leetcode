/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var curr = init;
    return {
        increment : function() {return ++curr},
        decrement : function() {return --curr},
        reset : function() {return (curr = init)}
    };
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */