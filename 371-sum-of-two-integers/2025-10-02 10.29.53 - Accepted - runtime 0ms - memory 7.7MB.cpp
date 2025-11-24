class Solution {
public:
    int getSum(int a, int b) {
        
        int carry = 0;
        int result = 0;
        int a1, b1, inter;
        int i = 0;
        for (int i = 0; i < 32; i++) {
            a1 = a & 1;
            b1 = b & 1;
            inter = a1 ^ b1;
            result |= (inter ^ carry) << i;
            carry = (a1 & b1) | (inter & carry);
            a >>= 1;
            b >>= 1;
            // std::cout << result << " " << a << " " << b << " " << carry << " " << i << "\n";
        }

        return result;
    }
};