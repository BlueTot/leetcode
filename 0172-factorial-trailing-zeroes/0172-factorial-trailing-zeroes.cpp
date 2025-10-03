class Solution {
public:
    int trailingZeroes(int n) {

        auto num_twos_fives = [&](int n) {
            vector<int> counter(2, 0);
            while (n % 2 == 0) {
                counter[0]++;
                n /= 2;
            }
            while (n % 5 == 0) {
                counter[1]++;
                n /= 5;
            }
            return counter;
        };

        vector<int> counter(2, 0);
        for (int i = 1; i <= n; i++) {
            vector<int> counts = num_twos_fives(i);
            counter[0] += counts[0];
            counter[1] += counts[1];
        }

        return min(counter[0], counter[1]);  
    }
};