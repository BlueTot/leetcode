class Solution {
public:
    int countGoodStrings(int low, int high, int zero, int one) {
        
        const int M = 1e9 + 7;
        vector<int> dp(high+1);

        dp[0] = 1;
        int total = 0;
        for (int i = 1; i < dp.size(); i++) {
            if (i >= zero)
                dp[i] = (dp[i] + dp[i-zero]) % M;
            if (i >= one)
                dp[i] = (dp[i] + dp[i-one]) % M;
            if (low <= i && i <= high)
                total = (total + dp[i]) % M;
        }

        return total;
    }
};