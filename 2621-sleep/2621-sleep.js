/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    var x = await new Promise((resolve) => setTimeout(resolve, millis));
    return x;
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */