class Solution {
public:
    int superPow(int a, vector<int>& b) {

        const int M = 1337;

        auto expM = [](long long a, long long n, int m) {
            int result = 1;
            while (n > 0) {
                if (n & 1)
                    result = (result * a) % m;
                a = (a * a) % m;
                n >>= 1;
            }
            return result;
        };

        int result = 1;
        for (int d : b) {
            result = expM(result, 10, M);
            result = (result * expM(a, d, M)) % M;
        }
        return result;
        
    }
};