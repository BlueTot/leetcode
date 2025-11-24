class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        for (int i = 0; i < 16; i++) {
            bool first = (n & (1 << i)) != 0;
            bool last = (n & (1 << (31 - i))) != 0;
            if (!first && last) {
                n |= (1 << i);
                n ^= (1 << (31-i));
            } else if (first && !last) {
                n ^= (1 << i);
                n |= (1 << (31-i));
            }
        }
        return n;
    }
};