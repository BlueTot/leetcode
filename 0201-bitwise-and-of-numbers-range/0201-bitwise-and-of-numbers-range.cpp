class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {

        // next upper bound is
        // 2**(i+1)-1. if right > upper bound then we have a switch.
        // so value is 0
        // if contained it is a 1

        int res = 0, suffix, next_upper;

        for (int i = 0; i < 32; i++) {

            // we only care about cases where left[i] is 1
            int shift = 1 << i;
            if ((left & shift) == 0)
                continue;

            // we compute the largest upper bound for which
            // the bit is the same
            // if right exceeds this bit then the AND will be 0
            // otherwise it will remain 1

            suffix = shift - 1;
            next_upper = left & (~suffix) | suffix;

            // set the bit
            if (right <= next_upper) {
                res |= shift;
            }  
        }

        return res;
        
    }
};